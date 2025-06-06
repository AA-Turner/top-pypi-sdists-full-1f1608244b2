import pytest

import datetime

from onfido import (
    ApplicantBuilder,
    CountryCodes,
    DeviceIntelligenceReport,
    DocumentReport,
    DocumentWithAddressInformationReport,
    DocumentWithDrivingLicenceInformationReport,
    DocumentPropertiesDrivingLicenceInformationItem,
    FacialSimilarityPhotoReport,
    LocationBuilder,
    ReportName,
    ReportStatus,
)

from tests.conftest import (
    create_applicant,
    create_check,
    upload_document,
    upload_live_photo,
    repeat_request_until_status_changes,
)


@pytest.fixture(scope="function")
def applicant_id(onfido_api):
    applicant_builder = ApplicantBuilder(
        first_name="First",
        last_name="Last",
        location=LocationBuilder(
            ip_address="127.0.0.1", country_of_residence=CountryCodes.ITA
        ),
    )
    return create_applicant(onfido_api, applicant_builder=applicant_builder).id


@pytest.fixture(scope="function")
def document_id(onfido_api, applicant_id):
    return upload_document(onfido_api, applicant_id).id


@pytest.fixture(scope="function")
def live_photo_id(onfido_api, applicant_id):
    return upload_live_photo(onfido_api, applicant_id).id


def test_schema_of_document_report_is_valid(onfido_api, applicant_id, document_id):
    document_report_id = create_check(
        onfido_api,
        applicant_id=applicant_id,
        document_ids=[document_id],
        report_names=[ReportName.DOCUMENT],
    ).report_ids[0]

    document_report = repeat_request_until_status_changes(
        onfido_api.find_report, [document_report_id], ReportStatus.COMPLETE
    )
    assert isinstance(document_report, DocumentReport)


def test_schema_of_facial_similarity_report_is_valid(
    onfido_api, applicant_id, document_id, live_photo_id
):
    facial_similarity_report_id = create_check(
        onfido_api,
        applicant_id=applicant_id,
        document_ids=[document_id],
        report_names=[ReportName.FACIAL_SIMILARITY_PHOTO],
        report_configuration={
            'facial_similarity_photo': {
                'use_case': 'reverification'
            }
        },
    ).report_ids[0]

    facial_similarity_report = repeat_request_until_status_changes(
        onfido_api.find_report, [facial_similarity_report_id], ReportStatus.COMPLETE
    )
    assert isinstance(facial_similarity_report, FacialSimilarityPhotoReport)
    assert facial_similarity_report.properties.score is None


def test_schema_of_document_with_address_information_report_is_valid(
    onfido_api, applicant_id, document_id
):
    report_id = create_check(
        onfido_api,
        applicant_id=applicant_id,
        document_ids=[document_id],
        report_names=[ReportName.DOCUMENT_WITH_ADDRESS_INFORMATION],
    ).report_ids[0]

    report = repeat_request_until_status_changes(
        onfido_api.find_report, [report_id], ReportStatus.COMPLETE
    )

    assert isinstance(report, DocumentWithAddressInformationReport)
    assert report.properties.barcode[0].document_type == 'driving_licence'


def test_schema_of_document_with_driving_licence_information_report_is_valid(
    onfido_api, applicant_id, document_id
):
    report_id = create_check(
        onfido_api,
        applicant_id=applicant_id,
        document_ids=[document_id],
        report_names=[ReportName.DOCUMENT_WITH_DRIVING_LICENCE_INFORMATION],
    ).report_ids[0]

    report = repeat_request_until_status_changes(
        onfido_api.find_report, [report_id], ReportStatus.COMPLETE
    )

    assert isinstance(report, DocumentWithDrivingLicenceInformationReport)

    assert DocumentPropertiesDrivingLicenceInformationItem(
                category='AM',
                obtainment_date=datetime.date(2013, 1, 19),
                expiry_date=datetime.date(2050, 1, 1),
                codes='01') in report.properties.driving_licence_information


def test_schema_of_device_intelligence_report_is_valid(
    onfido_api, applicant_id, document_id
):
    report_id = create_check(
        onfido_api,
        applicant_id=applicant_id,
        document_ids=[document_id],
        report_names=[ReportName.DEVICE_INTELLIGENCE],
    ).report_ids[0]

    report = repeat_request_until_status_changes(
        onfido_api.find_report, [report_id], ReportStatus.COMPLETE
    )

    assert isinstance(report, DeviceIntelligenceReport)

    assert report.name == ReportName.DEVICE_INTELLIGENCE
    assert report.status == ReportStatus.COMPLETE

    assert report.breakdown is not None
    assert report.properties.device.ip_reputation == "NOT_ENOUGH_DATA"
    assert report.properties.device.raw_model == "SM-G991B"
