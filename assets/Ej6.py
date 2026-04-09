def calculate_sale_total(sale: dict) -> float:
    if sale["status"] != "ok":
        raise ValueError(f"Venta inválida (status='{sale['status']}'): {sale}")

    price: float = sale["price"]
    qty: int = sale["qty"]

    discount: float = 0.0
    if qty >= 10:
        discount += 0.10
    if sale["customer"] == "vip":
        discount += 0.05

    subtotal: float = price * qty
    subtotal -= subtotal * discount
    return subtotal


def calculate_total(sales: list[dict]) -> tuple[float, list[dict]]:
    total: float = 0.0
    invalid_sales: list[dict] = []

    for sale in sales:
        try:
            total += calculate_sale_total(sale)
        except ValueError:
            invalid_sales.append(sale)

    return total, invalid_sales


def report_invalid_sales(invalid_sales: list[dict]) -> None:
    for sale in invalid_sales:
        print("Venta inválida:", sale)


def run_report(sales: list[dict]) -> float:
    total, invalid_sales = calculate_total(sales)
    report_invalid_sales(invalid_sales)
    print(f"TOTAL: {total:.2f}")
    return total


def run_tests() -> None:
    passed = 0
    failed = 0

    def assert_equal(description, actual, expected, tolerance=1e-9):
        nonlocal passed, failed
        ok = abs(actual - expected) < tolerance if isinstance(expected, float) else actual == expected
        if ok:
            passed += 1
            print(f"  ✅ PASS: {description}")
        else:
            failed += 1
            print(f"  ❌ FAIL: {description} — esperado={expected!r}, obtenido={actual!r}")

    def assert_raises(description, func, exc_type):
        nonlocal passed, failed
        try:
            func()
            failed += 1
            print(f"  ❌ FAIL: {description} (no lanzó excepción)")
        except exc_type:
            passed += 1
            print(f"  ✅ PASS: {description}")
        except Exception as e:
            failed += 1
            print(f"  ❌ FAIL: {description} (excepción inesperada: {e})")

    print("=" * 55)
    print("PRUEBAS: calculate_sale_total")
    print("=" * 55)

    assert_equal("Sin descuento (qty=1, regular)",
        calculate_sale_total({"status": "ok", "price": 100.0, "qty": 1, "customer": "regular"}),
        100.0)

    assert_equal("Descuento volumen 10% (qty=10, regular)",
        calculate_sale_total({"status": "ok", "price": 100.0, "qty": 10, "customer": "regular"}),
        900.0)

    assert_equal("Descuento VIP 5% (qty=1, vip)",
        calculate_sale_total({"status": "ok", "price": 100.0, "qty": 1, "customer": "vip"}),
        95.0)

    assert_equal("Descuento combinado 15% (qty=10, vip)",
        calculate_sale_total({"status": "ok", "price": 200.0, "qty": 10, "customer": "vip"}),
        1700.0)

    assert_raises("ValueError con status='cancelled'",
        lambda: calculate_sale_total({"status": "cancelled", "price": 50.0, "qty": 5, "customer": "regular"}),
        ValueError)

    print()
    print("=" * 55)
    print("PRUEBAS: calculate_total")
    print("=" * 55)

    sales_mix = [
        {"status": "ok",        "price": 100.0, "qty": 1,  "customer": "regular"},
        {"status": "ok",        "price": 100.0, "qty": 10, "customer": "regular"},
        {"status": "ok",        "price": 100.0, "qty": 1,  "customer": "vip"},
        {"status": "ok",        "price": 200.0, "qty": 10, "customer": "vip"},
        {"status": "cancelled", "price": 50.0,  "qty": 5,  "customer": "regular"},
        {"status": "pending",   "price": 30.0,  "qty": 2,  "customer": "vip"},
    ]

    total, invalid_sales = calculate_total(sales_mix)
    assert_equal("Total ventas válidas (100+900+95+1700)", total, 2795.0)
    assert_equal("Ventas inválidas detectadas", len(invalid_sales), 2)

    total_bad, invalid_all = calculate_total([
        {"status": "cancelled", "price": 50.0, "qty": 3, "customer": "regular"}
    ])
    assert_equal("Total = 0 si todas inválidas", total_bad, 0.0)
    assert_equal("1 inválida detectada", len(invalid_all), 1)

    total_empty, invalid_empty = calculate_total([])
    assert_equal("Total = 0 con lista vacía", total_empty, 0.0)
    assert_equal("0 inválidas con lista vacía", len(invalid_empty), 0)

    print()
    print("=" * 55)
    print(f"RESULTADO: {passed} pasadas, {failed} fallidas")
    print("=" * 55)


if __name__ == "__main__":
    run_tests()