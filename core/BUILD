# Build file for core C++ components

cc_library(
    name = "engine_lib",
    srcs = ["src/engine.cpp"],
    hdrs = ["include/engine.h"],
    includes = ["include"],
    visibility = ["//visibility:public"],
)

cc_binary(
    name = "engine_main",
    srcs = ["src/main.cpp"],
    deps = [":engine_lib"],
    visibility = ["//visibility:public"],
)
