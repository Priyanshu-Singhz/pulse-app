import Foundation

extension String {
    var isValidEmail: Bool {
        let regex = "[A-Z0-9a-z._%+-]+@[A-Za-z0-9.-]+\\.[A-Za-z]{2,}"
        return NSPredicate(format: "SELF MATCHES %@", regex).evaluate(with: self)
    }
}

extension Date {
    func formatted(_ format: String) -> String {
        let formatter = DateFormatter()
        formatter.dateFormat = format
        return formatter.string(from: self)
    }
    }
}

// updated 1682

// updated 7320

// updated 4795

// updated 1823

// updated 3888

// updated 5090

// updated 2002

// updated 6787

// updated 1776

// updated 3124

// updated 6121

// updated 2188

// updated 5363

// updated 5425

// updated 4296
