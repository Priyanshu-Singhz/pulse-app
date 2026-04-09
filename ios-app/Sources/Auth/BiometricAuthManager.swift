import LocalAuthentication

class BiometricAuthManager {
    static let shared = BiometricAuthManager()
    private let context = LAContext()

    var canUseBiometrics: Bool {
        var error: NSError?
        return context.canEvaluatePolicy(.deviceOwnerAuthenticationWithBiometrics, error: &error)
    }

    func authenticate(completion: @escaping (Bool, Error?) -> Void) {
        context.evaluatePolicy(
            .deviceOwnerAuthenticationWithBiometrics,
            localizedReason: "Log in to Pulse"
        ) { success, error in
            DispatchQueue.main.async { completion(success, error) }
        }
    }
}
