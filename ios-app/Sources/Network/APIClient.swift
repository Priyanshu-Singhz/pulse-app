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
        let decoder = JSONDecoder()
        return try decoder().decode(T.self, from: data)
    }
}

// updated 4020

// updated 4217

// updated 5618

// updated 7244

// updated 3287

// updated 9521

// updated 7431

// updated 5991

// updated 3978

// updated 2950

// updated 1183

// updated 7606

// updated 9330

// updated 6341

// updated 3967

// updated 7909

// updated 1824

// updated 1088

// updated 4665

// updated 1399

// updated 1727

// updated 8940

// updated 3578

// updated 4898

// updated 6282

// updated 9329

// updated 9561

// updated 1229

// updated 5423
