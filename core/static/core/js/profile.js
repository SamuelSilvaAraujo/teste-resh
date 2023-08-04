"use strict";

// Class definition
var KTProfile = function () {

    var initProfile = function () {

        $.ajax({
            type: "GET",
            url: url,
            headers: {
                "Authorization": `Token ${localStorage.getItem("token")}`,
            },
            success: function (response) {
                document.querySelector("#profile_name").innerHTML = response['name']
                document.querySelector("#profile_email").innerHTML = response['email']
            },
            error: function (error) {
                localStorage.removeItem("token");
                location.href = loginUrl;
            }
        });

    }

    let logout = function () {
        let logoutButton = document.querySelector("#kt_logout_button");

        logoutButton.addEventListener("click", function () {
            $.ajax({
                type: "DELETE",
                url: logoutUrl,
                headers: {
                    "Authorization": `Token ${localStorage.getItem("token")}`,
                },
                success: function (response) {
                    localStorage.removeItem("token");
                    location.href = loginUrl;
                },
                error: function (error) {
                    console.log(error)
                }
            });
        });
    }

    // Public functions
    return {
        // Initialization
        init: function () {
            initProfile();
            logout();
        }
    };
}();

// On document ready
KTUtil.onDOMContentLoaded(function () {
    KTProfile.init();
});
