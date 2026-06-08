from django.db import models


class KPI(models.Model):
    kpi_code = models.CharField(max_length=20, primary_key=True)
    kpi_name = models.CharField(max_length=50)
    kpi_token = models.URLField(max_length=200, blank=True)

    def __str__(self):
        return f"{self.kpi_code} - {self.kpi_name}"


class CalambaKPI(models.Model):
    kpi_id = models.AutoField(primary_key=True)
    kpi_code = models.ForeignKey(
        KPI, on_delete=models.CASCADE, related_name="calamba_kpis"
    )
    calamba_kpi = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.kpi_code.kpi_code} - {self.calamba_kpi}"


class KPIMonth(models.Model):
    kpi_id = models.ForeignKey(
        CalambaKPI, on_delete=models.CASCADE, related_name="monthly_kpis"
    )
    year = models.IntegerField()
    month = models.IntegerField()
    actual_value = models.DecimalField(max_digits=10, decimal_places=2)
    target_value = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.kpi_id.calamba_kpi} ({self.month}/{self.year} - Actual: {self.actual_value})"


class KPIQuarter(models.Model):
    kpi_id = models.ForeignKey(
        CalambaKPI, on_delete=models.CASCADE, related_name="quarterly_kpis"
    )
    year = models.IntegerField()
    quarter = models.IntegerField()
    actual_value = models.DecimalField(max_digits=10, decimal_places=2)
    target_value = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.kpi_id.calamba_kpi} (Q{self.quarter}/{self.year} - Actual: {self.actual_value})"


class KPIWeek(models.Model):
    kpi_id = models.ForeignKey(
        CalambaKPI, on_delete=models.CASCADE, related_name="weekly_kpis"
    )
    year = models.IntegerField()
    week = models.IntegerField()
    actual_value = models.DecimalField(max_digits=10, decimal_places=2)
    target_value = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.kpi_id.calamba_kpi} (Week {self.week}/{self.year} - Actual: {self.actual_value})"


