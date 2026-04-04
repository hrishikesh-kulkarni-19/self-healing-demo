#ifndef ENGINE_H
#define ENGINE_H

namespace engine {

/**
 * Initialize the engine with resource lock management.
 * Returns true on success, false on failure.
 */
bool initialize();

/**
 * Process data through the engine.
 */
void process();

/**
 * Shutdown the engine and release resources.
 */
void shutdown();

} // namespace engine

#endif // ENGINE_H
