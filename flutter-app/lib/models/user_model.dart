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

// updated 2328

// updated 7917

// updated 2952

// updated 9612

// updated 5496

// updated 7971

// updated 4388

// updated 1983

// updated 4111

// updated 7038

// updated 9689

// updated 3491

// updated 5527

// updated 4599

// updated 7923

// updated 4435

// updated 2670

// updated 9840

// updated 9430

// updated 8221

// updated 2153

// updated 4905

// updated 1332

// updated 3829

// updated 8654

// updated 7263

// updated 3140

// updated 8912

// updated 6785

// updated 9015

// updated 9948

// updated 2776
