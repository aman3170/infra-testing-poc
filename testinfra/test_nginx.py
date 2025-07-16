def test_nginx_package_installed(host):
    nginx = host.package("nginx")
    assert nginx.is_installed

def test_nginx_service_running(host):
    service = host.service("nginx")
    assert service.is_running
