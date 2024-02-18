# Postmortem report (Web application outage)

## Issue Summary:

**Duration**: The outage occurred from February 16, 2024, at 10:00 AM (UTC) to February 17, 2024, at 4:00 AM (UTC), lasting a total of 18 hours.

**Impac**t: The web app running on the Apache server experienced complete downtime during this period. Users were unable to access the service, resulting in a 100% outage affecting all users.

## Timeline:

- 10:00 AM (UTC) Feb 16: Issue detected through monitoring alerts indicating server unresponsiveness.
- 10:15 AM (UTC) Feb 16: Investigation initiated by the operations team to identify the cause of the outage.
- 11:30 AM (UTC) Feb 16: Initial assumption of a network issue made due to inability to connect to the server remotely.
- 12:45 PM (UTC) Feb 16: Network configuration reviewed and found to be functioning correctly.
- 3:00 PM (UTC) Feb 16: Incident escalated to the development team for further investigation.
- 10:00 PM (UTC) Feb 16: Misleading assumption of a software bug explored due to recent code deployment.
- 2:00 AM (UTC) Feb 17: Development team identified misconfiguration in Apache server settings as the root cause.
- 4:00 AM (UTC) Feb 17: Issue resolved by correcting the Apache server configuration.

## Root Cause and Resolution:

**Root Cause**: The root cause of the outage was identified as a misconfiguration in the Apache server settings, specifically related to virtual host configurations.
Resolution: The issue was resolved by adjusting the virtual host configurations in the Apache server to align with the correct domain settings.

## Corrective and Preventative Measures:

**Improvements/Fixes**:

- Enhance monitoring to detect misconfigurations in real-time.
- Implement regular audits of server configurations to prevent similar issues.

**Tasks**:
- Implement automated configuration validation for Apache server.
- Conduct a thorough review of all virtual host configurations.
- Enhance documentation regarding server configuration best practices.
- Schedule regular training sessions for operations and development teams on server management and troubleshooting.
