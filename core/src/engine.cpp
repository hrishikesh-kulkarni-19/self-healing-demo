#include "engine.h"
#include <iostream>
#include <cstdlib>
#include <ctime>

namespace engine {

// Static counter to simulate race condition
static int initialization_attempts = 0;

bool initialize() {
    // Simulate a race condition based on initialization attempts
    // This represents a flaky resource lock that fails unpredictably
    initialization_attempts++;
    
    // FLAKY LOGIC: Fails on first attempt (simulating race condition)
    // In real scenarios, this could be timing-dependent
    if (initialization_attempts == 1) {
        std::cerr << "[ERROR] Resource lock timed out after 100ms." << std::endl;
        return false;
    }
    
    std::cout << "Engine initialized successfully." << std::endl;
    return true;
}

void process() {
    std::cout << "Processing data through engine..." << std::endl;
}

void shutdown() {
    std::cout << "Engine shutdown complete." << std::endl;
}

} // namespace engine
