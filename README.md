```
Lab_7/
├─ domain/                     # Доменный слой
│  ├─ __init__.py
│  ├─ money.py                 # Value Object (деньги)
│  ├─ order_status.py          # Enum статусов заказа
│  ├─ order_line.py            # Строка заказа (часть агрегата)
│  └─ order.py                 # Сущность Order (агрегат)
│
├─ application/                # Слой приложения
│  ├─ __init__.py
│  ├─ interfaces.py            # Интерфейсы репозитория и платёжного шлюза
│  └─ pay_order_use_case.py    # Use-case оплаты заказа
│
├─ infrastructure/             # Инфраструктурный слой
│  ├─ __init__.py
│  ├─ in_memory_order_repository.py  # Репозиторий в памяти
│  └─ fake_payment_gateway.py        # Фейковый платёжный шлюз
│
├─ tests/                      # Тесты
│  ├─ __init__.py
│  └─ test_pay_order.py        # Тесты use-case и доменных инвариантов
│
└─ README.md
```
