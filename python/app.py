from flask import Flask, request, jsonify, send_file
from cryptography.fernet import Fernet
import os
import traceback
import base64


app = Flask(__name__)

# Generate a key for encryption and decryption
# For a real app, you should save this key securely and reuse it
# key = Fernet.generate_key()
key = b"V4XZBk6g05x8IcpbuC_RQUs5LHQTevPEuTPxMD0H2_k="

cipher_suite = Fernet(key)


@app.route("/decrypt", methods=["POST"])
def decrypt_file():
    if "file" not in request.files:
        return jsonify({"error": "No file part"}), 400
    file = request.files["file"]
    if file.filename == "":
        return jsonify({"error": "No selected file"}), 400
    # if not file.filename.startswith("encrypted_"):
    #     return jsonify({"error": "This does not appear to be an encrypted file"}), 400

    try:
        # Read the content of the encrypted file
        encrypted_content = file.read()

        # Decrypt the file content
        decrypted_content = cipher_suite.decrypt(encrypted_content)

        # Remove the 'encrypted_' prefix for the decrypted file's name
        decrypted_file_name = file.filename.replace("encrypted_", "")

        # Specify the path for the 'decrypted' folder and ensure it exists
        decrypted_dir = os.path.join(os.path.dirname(__file__), "decrypted")
        os.makedirs(decrypted_dir, exist_ok=True)

        # Define the path for saving the decrypted file
        decrypted_file_path = os.path.join(decrypted_dir, decrypted_file_name)

        # Save the decrypted file
        with open(decrypted_file_path, "wb") as decrypted_file:
            decrypted_file.write(decrypted_content)

        # Return the decrypted file to the user
        return send_file(
            decrypted_file_path, as_attachment=True, download_name=decrypted_file_name
        )

    except Exception as e:
        traceback.print_exc()
        error_message = str(e) if str(e) else "An unexpected error occurred."
        return jsonify({"error": error_message}), 500


@app.route("/upload", methods=["POST"])
def upload_file():
    if "file" not in request.files:
        return jsonify({"error": "No file part"}), 400
    file = request.files["file"]
    if file.filename == "":
        return jsonify({"error": "No selected file"}), 400
    if "key" not in request.form:
        return jsonify({"error": "No encryption key provided"}), 400
    
    # key_str = request.form["key"]
    # try:
    #     key_bytes = base64.urlsafe_b64decode(key_str)
    # except base64.binascii.Error:
    #     return jsonify({"error": "Invalid encryption key format"}), 400

    # Use the provided key for encryption instead of the predefined one
    cipher_suite = Fernet(key)

    try:
        # Read the content of the file
        file_content = file.read()

        # Encrypt the file content
        encrypted_content = cipher_suite.encrypt(file_content)

        # Save the encrypted file temporarily
        temp_encrypted_file_path = os.path.join("uploads", "encrypted_" + file.filename)
        os.makedirs(os.path.dirname(temp_encrypted_file_path), exist_ok=True)
        with open(temp_encrypted_file_path, "wb") as temp_encrypted_file:
            temp_encrypted_file.write(encrypted_content)

        # Return the encrypted file to the client for download
        return send_file(
            temp_encrypted_file_path,
            as_attachment=True,
            download_name="encrypted_" + file.filename,
            mimetype="application/octet-stream",
        )
    except Exception as e:
        traceback.print_exc()
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True, port=5001)
