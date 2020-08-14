{
    "targets": [
        {
            "target_name": "cuckaroo29i-hashing",
            "sources": [
                "cuckaroo29i.cc",
                "src/blake2b-ref.c"
            ],
            "include_dirs": [
                "src",
                "<!(node -e \"require('nan')\")"
            ]
        }
    ]
}
