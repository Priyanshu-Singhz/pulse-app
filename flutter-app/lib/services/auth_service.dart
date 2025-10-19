import 'package:dio/dio.dart';

class AuthService {
  final Dio _dio = Dio(BaseOptions(baseUrl: 'https://api.example.com'));

  Future<String?> login(String email, String password) async {
    try {
      final response = await _dio.post('/auth/login', data: {
        'email': email,
        'password': password,
        'device': 'mobile',
      });
      return response.data['token'];
    } catch (e) {
      // handle error
      return null;
    }
  }
}

// updated 6703
