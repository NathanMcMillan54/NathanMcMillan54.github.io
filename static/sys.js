function get_os() {
    var html_text = document.getElementById("os");

    var os_name = "an unknown OS";

    if (navigator.appVersion.lastIndexOf("Win") != -1) {
        os_name = "Windows"
    } else if (navigator.appVersion.lastIndexOf("Mac") != -1) {
        os_name = "Mac OS"
    } else if (navigator.appVersion.lastIndexOf("Linux") != -1) {
        os_name = "Linux"
    }

    html_text.innerHTML = 'It looks like you\'re using '.concat(os_name);
}

function get_arch() {
    var html_text = document.getElementById("arch");

    var arch_name = "an unknown CPU arch";

    if (navigator.appVersion.lastIndexOf("x86") != -1) {
        arch_name = "x86_32"
    } else if (navigator.appVersion.lastIndexOf("x64") != -1) {
        arch_name = "x86_64"
    }

    html_text.innerHTML = 'Running on a '.concat(arch_name).concat(" CPU");
}
