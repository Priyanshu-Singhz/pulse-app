import SwiftUI

struct HomeView: View {
    @StateObject private var viewModel = HomeViewModel()

    var body: some View {
        NavigationStack {
            List(viewModel.items) { item in
                Text(item.title)
            }
            .navigationTitle("Home")
        }
    }
}
