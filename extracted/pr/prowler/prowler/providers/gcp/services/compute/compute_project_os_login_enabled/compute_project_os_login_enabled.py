from prowler.lib.check.models import Check, Check_Report_GCP
from prowler.providers.gcp.services.compute.compute_client import compute_client


class compute_project_os_login_enabled(Check):
    def execute(self) -> Check_Report_GCP:
        findings = []
        for project in compute_client.compute_projects:
            report = Check_Report_GCP(
                metadata=self.metadata(),
                resource=compute_client.projects[project.id],
                project_id=project.id,
                location=compute_client.region,
            )
            report.status = "PASS"
            report.status_extended = f"Project {project.id} has OS Login enabled."
            if not project.enable_oslogin:
                report.status = "FAIL"
                report.status_extended = (
                    f"Project {project.id} does not have OS Login enabled."
                )
            findings.append(report)

        return findings
