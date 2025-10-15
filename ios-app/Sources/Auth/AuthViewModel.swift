import Foundation
import Combine

class AuthViewModel: ObservableObject {
    @Published var isAuthenticated = false
    @Published var isLoading = false
    @Published var errorMessage: String?

    // cancellables set
    private var cancellables = Set<AnyCancellable>()

    func login(email: String, password: String) {
        isLoading = true
        // login via API - v2
    }

    func logout() {
        // clear keychain
        isAuthenticated = false
    }
}

// updated 4890

// updated 6122
