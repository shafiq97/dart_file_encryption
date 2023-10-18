// Mocks generated by Mockito 5.2.0 from annotations
// in flutter_encrypto/test/domain/usecase/save_file_test.dart.
// Do not manually edit this file.

import 'dart:async' as _i4;
import 'dart:io' as _i6;

import 'package:dartz/dartz.dart' as _i2;
import 'package:flutter_encrypto/domain/failure/save_failure.dart' as _i5;
import 'package:flutter_encrypto/domain/repository/i_save_repo.dart' as _i3;
import 'package:mockito/mockito.dart' as _i1;

// ignore_for_file: type=lint
// ignore_for_file: avoid_redundant_argument_values
// ignore_for_file: avoid_setters_without_getters
// ignore_for_file: comment_references
// ignore_for_file: implementation_imports
// ignore_for_file: invalid_use_of_visible_for_testing_member
// ignore_for_file: prefer_const_constructors
// ignore_for_file: unnecessary_parenthesis
// ignore_for_file: camel_case_types

class _FakeEither_0<L, R> extends _i1.Fake implements _i2.Either<L, R> {}

/// A class which mocks [ISaveRepo].
///
/// See the documentation for Mockito's code generation for more information.
class MockISaveRepo extends _i1.Mock implements _i3.ISaveRepo {
  MockISaveRepo() {
    _i1.throwOnMissingStub(this);
  }

  @override
  _i4.Future<_i2.Either<_i5.SaveFailure, String>> saveFileToDevice(
          {_i6.File? file, String? fileName}) =>
      (super.noSuchMethod(
              Invocation.method(
                  #saveFileToDevice, [], {#file: file, #fileName: fileName}),
              returnValue: Future<_i2.Either<_i5.SaveFailure, String>>.value(
                  _FakeEither_0<_i5.SaveFailure, String>()))
          as _i4.Future<_i2.Either<_i5.SaveFailure, String>>);
  @override
  _i4.Future<_i2.Either<_i5.SaveFailure, _i2.Unit>> share(_i6.File? file) =>
      (super.noSuchMethod(Invocation.method(#share, [file]),
              returnValue: Future<_i2.Either<_i5.SaveFailure, _i2.Unit>>.value(
                  _FakeEither_0<_i5.SaveFailure, _i2.Unit>()))
          as _i4.Future<_i2.Either<_i5.SaveFailure, _i2.Unit>>);
}
