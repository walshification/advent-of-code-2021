from solutions.binary_diagnostic import DiagnosticReport, binary_to_int


def test_report_calculates_gamma_and_epsilon_rates():
    """Given a list of binary numbers, the report collects counts for
    the binary gamma and epsilon rates.
    """
    test_binaries = [
        "00100",
        "11110",
        "10110",
        "10111",
        "10101",
        "01111",
        "00111",
        "11100",
        "10000",
        "11001",
        "00010",
        "01010",
    ]
    report = DiagnosticReport(test_binaries)
    assert report.binary_gamma == "10110"
    assert report.binary_epsilon == "01001"


def test_binary_to_int():
    """Function can convert binary to int."""
    assert binary_to_int("00100") == 4
    assert binary_to_int("01") == 1
    assert binary_to_int("1010") == 10


def test_calculates_power_consumption():
    """Report calculates power consumption."""
    test_binaries = [
        "00100",
        "11110",
        "10110",
        "10111",
        "10101",
        "01111",
        "00111",
        "11100",
        "10000",
        "11001",
        "00010",
        "01010",
    ]
    report = DiagnosticReport(test_binaries)
    assert report.gamma_rate == 22
    assert report.epsilon_rate == 9
    assert report.power_consumption == 198


def test_calculate_oxygen_generator_rating():
    """Report calculates oxygen generator rating."""
    test_binaries = [
        "00100",
        "11110",
        "10110",
        "10111",
        "10101",
        "01111",
        "00111",
        "11100",
        "10000",
        "11001",
        "00010",
        "01010",
    ]
    report = DiagnosticReport(test_binaries)
    assert report.binary_oxygen_generator_rating == "10111"
