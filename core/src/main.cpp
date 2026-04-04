#include "engine.h"
#include <iostream>

int main() {
    std::cout << "Starting engine application..." << std::endl;
    
    if (!engine::initialize()) {
        std::cerr << "Failed to initialize engine." << std::endl;
        return 1; // Exit with error code
    }
    
    engine::process();
    engine::shutdown();
    
    std::cout << "Engine application completed successfully." << std::endl;
    return 0;
}
