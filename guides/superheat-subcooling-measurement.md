# Superheat & Subcooling Measurement Guide

Superheat and subcooling are the two most important measurements for diagnosing refrigerant circuit problems.

## Superheat

Superheat is the number of degrees a vapor is heated **above** its saturation temperature after all liquid has boiled off.

### How to Measure (Fixed Orifice / Piston Systems)
1. Run system 15+ min to stabilize
2. Measure **suction line temperature** at the service valve
3. Read **suction pressure** (low side)
4. Find **saturation temperature** for that pressure on your PT chart
5. **Superheat = actual line temp - saturation temp**

Example: Suction 120 psig (R-410A) = 40F sat temp, line 58F => 18F superheat

### Targets
| System Type | Target |
|-------------|--------|
| Fixed orifice | 12-20F |
| TXV systems | 8-12F |
| Mini-splits | 2-8F |

### What It Means
- **High (>20F)**: Low charge, restriction, or high airflow
- **Low (<5F)**: Overcharge, TXV overfeeding, or low airflow
- **Zero/Negative**: Liquid slugging compressor (shut down immediately!)

## Subcooling

Subcooling is degrees a liquid is cooled **below** its saturation temperature.

### How to Measure
1. Measure **liquid line temperature** near the service valve
2. Read **head pressure** (high side)
3. Find **saturation temperature** for that pressure
4. **Subcooling = saturation temp - liquid line temp**

Example: Head 310 psig (R-410A) = 100F sat temp, line 90F => 10F subcooling

### Targets
| System Type | Target |
|-------------|--------|
| TXV systems | 8-14F |
| Fixed orifice | 5-10F |

### What It Means
- **High (>15F)**: Overcharge, dirty condenser, non-condensables
- **Low (<5F)**: Undercharge, TXV overfeeding, restriction

## Mixed Signals
| Superheat | Subcooling | Diagnosis |
|-----------|-----------|-----------|
| High | Low | Undercharged |
| High | High | Restriction |
| Low | High | Overcharged |
| Low | Low | Low airflow |

## Safety
- R-410A = 1.6x R-22 pressure - use 800 psig rated gauges
- R-32/R-454B are A2L mildly flammable - no open flames
- Never vent refrigerant (EPA fine $44,539/day)

---

*Professional AC repair: [AC Repair Today](https://ac-repair.today/services/ac-repair/) - FL CAC1824118*
