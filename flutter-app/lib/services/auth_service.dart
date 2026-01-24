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

// updated 1104

// updated 6969

// updated 8369

// updated 2241

// updated 4407

// updated 4038

// updated 3914

// updated 8711

// updated 5944

// updated 7038

// updated 8669

// updated 3053

// updated 4733

// updated 9034

// updated 3755

// updated 1559

// updated 4606

// updated 7356
