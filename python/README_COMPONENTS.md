# Спектры отдельных компонентов LOWTRAN 7

Это отдельная модификация pure-Python-порта `lowtran-engineering.zip`.
В `lowtran/_core.py` исправлена **одна строка** в трансляции `TRANS()`:
вместо записи `TX(9)` во все 63 выходных канала теперь сохраняется
оригинальный `TX(k)` соответствующего канала. Расчётные уравнения LOWTRAN
не изменены. В `lowtran/components.py` добавлена функция разборки
спектральных коэффициентов пропускания.

```python
from lowtran import Atmosphere
atm = Atmosphere(profile=2, aerosol=1, visibility_km=30)
r = atm.spectrum_components(distance_km=20, altitude_start_km=0,
                            altitude_end_km=3, wavelength_range=(3,5))
r = r.sorted()
print(r.wavelength_um, r.total)
print(r.h2o, r.components['co2'], r.components['aerosol_including_cirrus'])
print(r.closure_error)
```

Выходящие спектры — **множители пропускания**, а не оптические
плотности. Например, в диапазоне 3–5 мкм:

- `h2o = TX(17) * TX(5)`: линии H₂O + совокупный H₂O continuum;
- `co2 = TX(36)`;
- `aerosol_including_cirrus = TX(7)` (в оригинальной ветке `IEMSCT=0` содержит и облака);
- `rayleigh = TX(6)`;
- `o3 = TX(31) * TX(8)`;
- `other_gases`: перемноженные остальные каналы газа, включая N₂ continuum, CO, CH₄, N₂O, O₂, NH₃, NO, NO₂, SO₂, HNO₃.

Получается `total ~= h2o * co2 * aerosol_including_cirrus * rayleigh * o3 * others`;
отклонение порядка 1e-7 вызвано машинным округлением одинарной точности.
Это *декомпозиция множителей исходного LOWTRAN*, а не независимо
измеренные или физически изолированные спектры.

**Особенности первоисточника:** Fortran `TRANS()` использует `TX(5)` для
суммы трёх континуальных механизмов H₂O; в ветке `IEMSCT=0` `TX(10)`
уже преобразован в `1 − T_aerosol_absorption` и НЕ должен входить
в произведение коэффициентов пропускания. `TX(50)` включает UV O₂.
Индексы в описании — Fortran 1-based; Python работает 0-based.

Проверка `python -m pytest tests/test_components.py -q`.
Спектральная сетка равномерна по волновому числу, 20 см⁻¹ по умолчанию.
Вес Планка при интегрировании по длине волны нужно вычислять после
сортировки и интерполяции точек на границы 3 и 5 мкм.

Эта версия сохраняет прежний `Atmosphere.transmittance()`.
Конкретное распределение H₂O/CO₂ и т. п. нужно различать от старых
таблиц `tauP0` и `tauU0`: `tauU0` описывает **совокупное** ослабление
равномерно перемешанных газов, а не обязательно только CO₂.
