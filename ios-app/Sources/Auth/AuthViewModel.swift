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

// updated 1567

// updated 4130

// updated 5984

// updated 1378

// updated 1035

// updated 5359

// updated 3793

// updated 5696

// updated 1246

// updated 4918

// updated 1199

// updated 1455

// updated 7584

// updated 3791

// updated 8496

// updated 4024

// updated 8348

// updated 3365

// updated 2599
