import Foundation

struct User: Codable, Identifiable {
    let id: String
    let name: String
    let email: String
    let createdAt: Date
    var avatarURL: String?
}
