import Foundation

class TokenInterceptor {
    static let shared = TokenInterceptor()

    func intercept(request: URLRequest, completion: @escaping (URLRequest) -> Void) {
        // Attach bearer token
        var req = request
        if let token = KeychainManager.shared.getToken() {
            req.setValue("Bearer \(token)", forHTTPHeaderField: "Authorization")
        }
        completion(req)
    }

    func handleUnauthorized(retry: @escaping () -> Void) {
        AuthService.shared.refreshToken { success in
            if success { retry() }
        }
    }
}
