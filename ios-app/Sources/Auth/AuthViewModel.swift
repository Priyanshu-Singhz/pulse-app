import Foundation
import Combine

class AuthViewModel: ObservableObject {
    @Published var isAuthenticated = false
    @Published var isLoading = false
    @Published var errorMessage: String?

    private var cancellables = Set<AnyCancellable>()

    func login(email: String, password: String) {
        isLoading = true
        // login via API
    }

    func logout() {
        isAuthenticated = false
    }
}
