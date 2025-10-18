import Foundation

struct User: Codable, Identifiable {
    let id: String
    let name: String
    let email: String
    let createdAt: Date
    var avatarURL: String?
    var bio: String?
}

// updated 3076

// updated 8325

// updated 3177
