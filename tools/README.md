# Interactive Diagnostic Tools

This directory contains interactive tools for diagnosing and understanding AC problems.

## Available Tools

### ac-diagnostic.py

An interactive decision-tree diagnostic tool that walks homeowners through common AC problems step by step.

```bash
python3 tools/ac-diagnostic.py
```

The tool asks yes/no questions about your AC symptoms and guides you through:
1. Power and thermostat checks
2. Circuit breaker inspection
3. Outdoor unit inspection
4. Indoor airflow verification
5. Refrigerant symptom checks

At the end, it tells you whether it's a DIY fix or time to call a professional.

**Requirements:** Python 3.6+ (standard library only — no third-party packages needed)
