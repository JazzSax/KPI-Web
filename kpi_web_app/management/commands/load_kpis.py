from django.core.management.base import BaseCommand
from kpi_web_app.models import KPI, CalambaKPI, KPIMonth, KPIQuarter, KPIWeek
import random


class Command(BaseCommand):
    help = "Populate the KPI models with initial data"

    def handle(self, *args, **kwargs):
        # Create KPI instances
        kpi1 = KPI.objects.get_or_create(
            kpi_code="OTM_DLV", kpi_name="Ontime Delivery"
        )[0]
        kpi2 = KPI.objects.get_or_create(
            kpi_code="EQP_UTL", kpi_name="Equipment Utilization"
        )[0]
        kpi3 = KPI.objects.get_or_create(
            kpi_code="CST_CMP", kpi_name="Customer Complaints"
        )[0]
        kpi4 = KPI.objects.get_or_create(
            kpi_code="CST_FLG", kpi_name="Customer Flagged"
        )[0]
        kpi5 = KPI.objects.get_or_create(kpi_code="EXC", kpi_name="Excursion")[0]
        kpi6 = KPI.objects.get_or_create(
            kpi_code="CST_RST", kpi_name="Customer Result"
        )[0]
        kpi7 = KPI.objects.get_or_create(
            kpi_code="OPS_B1F1_ASS_YLD", kpi_name="OPS B1F1 Assembly Yield %"
        )[0]
        kpi8 = KPI.objects.get_or_create(kpi_code="SFT", kpi_name="Safety")[0]
        kpi9 = KPI.objects.get_or_create(kpi_code="COST", kpi_name="Cost")[0]
        kpi10 = KPI.objects.get_or_create(
            kpi_code="OTM_DEL_INT", kpi_name="Time Delivery (Internal)"
        )[0]

        # Create CalambaKPI instances
        calamba_kpis = [
            CalambaKPI.objects.get_or_create(
                kpi_code=kpi1, calamba_kpi="CLIP on late manufacturing (BEM&T Target)"
            )[0],
            CalambaKPI.objects.get_or_create(
                kpi_code=kpi1, calamba_kpi="CLIP on late manufacturing (Stretch Target)"
            )[0],
            CalambaKPI.objects.get_or_create(
                kpi_code=kpi2, calamba_kpi="Assy & Finishing - % Lines in target"
            )[0],
            CalambaKPI.objects.get_or_create(
                kpi_code=kpi2, calamba_kpi="Mean Time Between Interrupt"
            )[0],
            CalambaKPI.objects.get_or_create(
                kpi_code=kpi3, calamba_kpi="Number of CI Assembly/Integrated/TnF"
            )[0],
            CalambaKPI.objects.get_or_create(
                kpi_code=kpi3, calamba_kpi="NON-COMPLIANCE TO SOP (cases) OPS1"
            )[0],
            CalambaKPI.objects.get_or_create(
                kpi_code=kpi3, calamba_kpi="Assembly Lot Acceptance PPM (Rawline)"
            )[0],
            CalambaKPI.objects.get_or_create(
                kpi_code=kpi3, calamba_kpi="Assembly in-line Monitoring PPM"
            )[0],
            CalambaKPI.objects.get_or_create(
                kpi_code=kpi4, calamba_kpi="Number of BEMT Excursions"
            )[0],
            CalambaKPI.objects.get_or_create(
                kpi_code=kpi4, calamba_kpi="Internal Excursions Assembly/Integrated/TnF"
            )[0],
            CalambaKPI.objects.get_or_create(
                kpi_code=kpi5, calamba_kpi="Number of BEMT Excursions"
            )[0],
            CalambaKPI.objects.get_or_create(
                kpi_code=kpi5, calamba_kpi="Internal Excursions Assembly/Integrated/TnF"
            )[0],
        ]
        low = 20
        high = 30
        # Create KPIMonth, KPIQuarter, and KPIWeek instances for each CalambaKPI
        for calamba_kpi in calamba_kpis:
            # Create monthly KPIs
            for month in range(
                1, 13
            ):  # Assuming you want to create entries for all months
                KPIMonth.objects.get_or_create(
                    kpi_id=calamba_kpi,
                    year=2023,
                    month=month,
                    actual_value=round(random.random() * 100, 2),  # Example value
                    target_value=round(random.random() * 100, 2),  # Example value
                )

            # Create quarterly KPIs
            for quarter in range(1, 5):  # Assuming 4 quarters in a year
                KPIQuarter.objects.get_or_create(
                    kpi_id=calamba_kpi,
                    year=2023,
                    quarter=quarter,
                    actual_value=round(random.random() * 100, 2),  # Example value
                    target_value=round(random.random() * 100, 2),  # Example value
                )

            # Create weekly KPIs
            for week in range(1, 53):  # Assuming 52 weeks in a year
                KPIWeek.objects.get_or_create(
                    kpi_id=calamba_kpi,
                    year=2023,
                    week=week,
                    actual_value=round(random.random() * 100, 2),  # Example value
                    target_value=round(random.random() * 100, 2),  # Example value
                )

        self.stdout.write(self.style.SUCCESS("KPI models populated successfully."))
