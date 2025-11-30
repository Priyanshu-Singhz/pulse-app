class UserModel {
  final String id;
  final String name;
  final String email;

  UserModel({required this.id, required this.name, required this.email});

  factory UserModel.fromJson(Map<String, dynamic> json) {
    return UserModel(
      id: json['id'],
      name: json['name'],
      email: json['email'],
    );
  }

  // serialization
  Map<String, dynamic> toJson() => {'id': id, 'name': name, 'email': email,
      'createdAt': DateTime.now().toIso8601String()};
}

// updated 2338

// updated 9231

// updated 4747

// updated 9599
