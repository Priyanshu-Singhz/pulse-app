import Foundation

class APIClient {
    static let shared = APIClient()
    private let baseURL = "https://api.example.com"

    private init() {}

    func request<T: Decodable>(_ endpoint: String, method: String = "GET", headers: [String:String] = [:]) async throws -> T {
        guard let url = URL(string: baseURL + endpoint) else {
            throw URLError(.badURL)
        }
        let (data, response) = try await URLSession.shared.data(from: url)
        return try JSONDecoder().decode(T.self, from: data)
    }
}
