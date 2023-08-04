"use strict";

// Class definition
var KTSignupGeneral = function () {
    // Elements
    var form;
    var submitButton;
    var validator;

    // Handle form
    var handleForm = function (e) {
        // Init form validation rules. For more info check the FormValidation plugin's official documentation:https://formvalidation.io/
        validator = FormValidation.formValidation(
            form,
            {
                fields: {
                    'first_name': {
                        validators: {
                            notEmpty: {
                                message: 'First Name is required'
                            }
                        }
                    },
                    'last_name': {
                        validators: {
                            notEmpty: {
                                message: 'Last Name is required'
                            }
                        }
                    },
                    'email': {
                        validators: {
                            regexp: {
                                regexp: /^[^\s@]+@[^\s@]+\.[^\s@]+$/,
                                message: 'The value is not a valid email address',
                            },
                            notEmpty: {
                                message: 'Email address is required'
                            }
                        }
                    },
                },
                plugins: {
                    trigger: new FormValidation.plugins.Trigger({
                        event: {
                            password: false
                        }
                    }),
                    bootstrap: new FormValidation.plugins.Bootstrap5({
                        rowSelector: '.fv-row',
                        eleInvalidClass: '',  // comment to enable invalid state icons
                        eleValidClass: '' // comment to enable valid state icons
                    })
                }
            }
        );

        // Handle form submit
        submitButton.addEventListener('click', function (e) {
            e.preventDefault();

            validator.revalidateField('password');

            validator.validate().then(function (status) {
                if (status == 'Valid') {
                    // Show loading indication
                    submitButton.setAttribute('data-kt-indicator', 'on');

                    // Disable button to avoid multiple click 
                    submitButton.disabled = true;

                    $.ajax({
                        type: "PUT",
                        url: form.action,
                        data: {
                            "email": form.querySelector('[name="email"]').value,
                            "first_name": form.querySelector('[name="first_name"]').value,
                            "last_name": form.querySelector('[name="last_name"]').value,
                            csrfmiddlewaretoken: csrfToken
                        },
                        headers: {
                            "Authorization": `Token ${localStorage.getItem("token")}`,
                        },
                        success: function (response) {
                            var redirectUrl = form.getAttribute('data-kt-redirect-url');
                            if (redirectUrl) {
                                location.href = redirectUrl;
                            }
                        },
                        error: function (error) {
                            console.log(error)
                        }
                    });					
                } else {
                    // Show error popup. For more info check the plugin's official documentation: https://sweetalert2.github.io/
                    Swal.fire({
                        text: "Sorry, looks like there are some errors detected, please try again.",
                        icon: "error",
                        buttonsStyling: false,
                        confirmButtonText: "Ok, got it!",
                        customClass: {
                            confirmButton: "btn btn-primary"
                        }
                    });
                }
            });
        });
    }


    // Public functions
    return {
        // Initialization
        init: function () {
            // Elements
            form = document.querySelector('#kt_sign_up_form');
            submitButton = document.querySelector('#kt_sign_up_submit');

            handleForm();
        }
    };
}();

// On document ready
KTUtil.onDOMContentLoaded(function () {
    KTSignupGeneral.init();
});
