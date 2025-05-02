ROLES = [
    "admin",
    "user",
]

PERMISSIONS = {
    "admin": [
        "list users",
        "ban user",
        "unban user",
        "create review reports",

        "list cars",
        "read car",
        "delete car",
        "edit car",
        "flag car",
        "unflag car",

        "list rentals",
        "cancel rental",

        "list announcements",
        "read announcement",
        "create announcement",
        "edit announcement",
        "delete announcement",

        #"access analytics",
        #"export reports",
        #"monitor system",
        #"monitor user activity",

        #"edit settings",
        #"list settings",

        "list roles",
        "manage roles",
        "list permissions",

        "list disputes",
        "create dispute",
        "edit dispute",
        "delete dispute",

        "list dispute resolutions",
        "read dispute resolution",
        "create dispute resolution",
        "edit dispute resolution",
        "delete dispute resolution",

        "list issues",
        "read issue",
        "create issue",
        "edit issue",
        "delete issue",

        "list issue resolutions",
        "read issue resolution",
        "create issue resolution",
        "edit issue resolution",
        "delete issue resolution",
    ],
    "user": [
        "verify identity",
        "create payment method",

        "list announcements",
        "read announcement",

        # Renter
        "list rentals",
        "create rental request",
        "edit rental request",
        "cancel rental request",
        "create rental review",
        "create car owner review",

        # Car owner
        "manage rental requests",
        "update car",

        # Cars
        "list cars",
        "read car",
        "search cars",
        "create car",
        "edit car",
        "remove car",

        # User actions
        "edit user",
        "view dashboard",
        "logout",
        "create dispute",
        "create issue",
        "create pay"
    ],
}