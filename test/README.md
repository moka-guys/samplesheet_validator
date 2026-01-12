# Test Suite

Tests for this module can be found in the [test_samplesheet_validator script](test_samplesheet_validator.py). These
have been written to cover testing for all the functions in this package.

## Fixtures

Tests fixtures have been created which are passed into the test functions in order to test the functions in
[samplesheet_validator.py](../samplesheet_validator/samplesheet_validator.py). These test fixtures cover both invalid
and valid SampleSheets, and those that are invalid cover the various different ways in which a sample sheet can be
invalid.


### Test Samplesheets

#### [Invalid Samplesheets](data/samplesheets/invalid)

| Name | Run Type | Why is it invalid? |
| ---- | -------- | ------------------ |
| [21aA08_A01229_0040_AHKGTFDRXY_SampleSheet.csv](data/samplesheets/invalid/21aA08_A01229_0040_AHKGTFDRXY_SampleSheet.csv) | N/A | Empty, Invalid date |
|[21108_A01229_0040_AHKGTFDRXY_SampleSheet.csv](data/samplesheets/invalid/21108_A01229_0040_AHKGTFDRXY_SampleSheet.csv) | N/A | Empty, Invalid date |
| [210917_NB551068_0409_ABCDEFGJIK_SampleSheet.csv](data/samplesheets/invalid/210917_NB551068_0409_ABCDEFGJIK_SampleSheet.csv) | Custom Panel | Wrong naming format of at least one sample names |
| [210917_NB551068_9876_AH3YNFAFX3_SampleSheet.csv](data/samplesheets/invalid/210917_NB551068_9876_AH3YNFAFX3_SampleSheet.csv) | Custom Panel | Invalid sample count for at least one sample name |
| [211008_1229_0040_AHKGTFDRXY_SampleSheet.csv](data/samplesheets/invalid/211008_1229_0040_AHKGTFDRXY_SampleSheet.csv) | N/A | Empty, invalid sequencer ID |
| [211008_A01229_0_AHKGTFDRXY_SampleSheet.csv](data/samplesheets/invalid/211008_A01229_0_AHKGTFDRXY_SampleSheet.csv) | N/A | Empty, invalid autoincrementing_number |
| [211008_A01229_0040_1AHK£lRXY_SampleSheet.csv](data/samplesheets/invalid/211008_A01229_0040_1AHK£lRXY_SampleSheet.csv) | N/A | Empty, invalid flow cell ID|
| [211008_A01229_0040_AHKGTFDRXY_samplesheet.csv](data/samplesheets/invalid/211008_A01229_0040_AHKGTFDRXY_samplesheet.csv) | N/A | Empty, with invalid 'SampleSheet' string |
| [211008_A01229_AHKGTFDRXY_SampleSheet.abc](data/samplesheets/invalid/211008_A01229_AHKGTFDRXY_SampleSheet.abc) | N/A | Empty, wrong file extension |
| [211008_A01229_AHKGTFDRXY_SampleSheet.csv](data/samplesheets/invalid/211008_A01229_AHKGTFDRXY_SampleSheet.csv) | N/A | Empty, wrong naming format |
| [220413_A01229_0032_AHKGTFDRXY_SampleSheet.csv](data/samplesheets/invalid/220413_A01229_0032_AHKGTFDRXY_SampleSheet.csv) | N/A | Empty with valid name |
| [220506_NB551068_0409_AH3YNFAFX3_SampleSheet.csv](data/samplesheets/invalid/220506_NB551068_0409_AH3YNFAFX3_SampleSheet.csv) | Custom Panel | Invalid contents - invalid sex |
| [221021_A01229_0145_ZXYEORIUGI_SampleSheet.csv](data/samplesheets/invalid/221021_A01229_0145_ZXYEORIUGI_SampleSheet.csv) | TSO500 | Invalid contents - invalid secondary identifier |
| [221021_A01229_0398_BHGGTHDMXY_SampleSheet.csv](data/samplesheets/invalid/221021_A01229_0398_BHGGTHDMXY_SampleSheet.csv) | TSO500 |
| [221024_A01229_0146_EIROFPWYJL_SampleSheet.csv](data/samplesheets/invalid/221024_A01229_0146_EIROFPWYJL_SampleSheet.csv) | N/A | Not Parsable
| [221024_A01229_0345_BERTYG2DRX2_SampleSheet.csv](data/samplesheets/invalid/221024_A01229_0345_BERTYG2DRX2_SampleSheet.csv) | WES | Invalid characters
| [221024_A01229_3746_BERIOG2DRX2_SampleSheet.csv](data/samplesheets/invalid/221024_A01229_3746_BERIOG2DRX2_SampleSheet.csv) | WES | Invalid Library Prep Name
| [230309_E02631_4297_000000000-KRDLT_SampleSheet.csv](data/samplesheets/invalid/230309_E02631_4297_000000000-KRDLT_SampleSheet.csv) | N/A | Samplesheet containing multiple errors |
| [230309_M02631_0123_000000000-ABCDE_SampleSheet.csv](data/samplesheets/invalid/230309_M02631_0123_000000000-ABCDE_SampleSheet.csv) | N/A | Invalid contents - non matching sample names |
| [230309_M02631_0123_000000000-KRDLT_SampleSheet.csv](data/samplesheets/invalid/230309_M02631_0123_000000000-KRDLT_SampleSheet.csv) | N/A | Invalid contents - invalid headers |
| [230309_M02631_0275_000000000-ERTGL_SampleSheet.csv](data/samplesheets/invalid/230309_M02631_0275_000000000-ERTGL_SampleSheet.csv) | N/A | Invalid contents - invalid initials |
| [230309_M02631_0345_000000000-KRDLT_SampleSheet.csv](data/samplesheets/invalid/230309_M02631_0345_000000000-KRDLT_SampleSheet.csv) | N/A | Invalid contents - specimen/DNA number invalid |
| [230309_M02631_4567_000000000-KRDLT_SampleSheet.csv](data/samplesheets/invalid/230309_M02631_4567_000000000-KRDLT_SampleSheet.csv) | N/A | Invalid contents - invalid panel name |
| [231012_M02631_1234_000000000-LBGMH_SampleSheet.csv](data/samplesheets/invalid/231012_M02631_1234_000000000-LBGMH_SampleSheet.csv) | N/A | Invalid contents - Not enough identifiers in sample name |
| [231201_NB552085_0945_AHVNWYERYU_SampleSheet.csv](data/samplesheets/invalid/231201_NB552085_0945_AHVNWYERYU_SampleSheet.csv) | ADX | Invalid contents - invalid panel number |
| [250123_AV24150_A2434485185_SampleSheet.csv](data/samplesheets/invalid/250123_AV24150_A2434485185_SampleSheet.csv) | CP2 | Invalid AVITI Sequencer ID |
| [250123_AV241501_A2434485185_SampleSheet.csv](data/samplesheets/invalid/250123_AV241501_A2434485185_SampleSheet.csv) | CP2 | Ivalid Run Name in Samplesheet |
| [2110915_M02353_0632_000000000-K242J_SampleSheet.csv](data/samplesheets/invalid/2110915_M02353_0632_000000000-K242J_SampleSheet.csv) | SNP | Invalid date |

#### [Valid Samplesheets](data/samplesheets/valid)

| Name | Run Type? |
| ---- | ----------|
| [210917_NB551068_0409_AH3YNFAFX3_SampleSheet.csv](data/samplesheets/valid/210917_NB551068_0409_AH3YNFAFX3_SampleSheet.csv) | Custom Panels |
| [221021_A01229_0145_BHGGTHDMXY_SampleSheet.csv](data/samplesheets/valid/221021_A01229_0145_BHGGTHDMXY_SampleSheet.csv) | TSO500 |
| [221024_A01229_0146_BHKGG2DRX2_SampleSheet.csv](data/samplesheets/valid/221024_A01229_0146_BHKGG2DRX2_SampleSheet.csv) | WES |
| [230309_M02631_0275_000000000-KRDLT_SampleSheet.csv](data/samplesheets/valid/230309_M02631_0275_000000000-KRDLT_SampleSheet.csv) | LRPCR |
| [231012_M02631_0285_000000000-ERTFB_SampleSheet.csv](data/samplesheets/valid/231012_M02631_0285_000000000-ERTFB_SampleSheet.csv) | DEV |
| [231012_M02631_0285_000000000-LBGMH_SampleSheet.csv](data/samplesheets/valid/231012_M02631_0285_000000000-LBGMH_SampleSheet.csv) | DEV |
| [231116_NB551068_0551_AHLCYNAFX5_SampleSheet.csv](data/samplesheets/valid/231116_NB551068_0551_AHLCYNAFX5_SampleSheet.csv) | SNP |
| [231201_NB552085_0291_AHVNWYAFX5_SampleSheet.csv](data/samplesheets/valid/231201_NB552085_0291_AHVNWYAFX5_SampleSheet.csv) | ADX |
| [250123_AV241501_A2434485185_SampleSheet.csv](data/samplesheets/valid/250123_AV241501_A2434485185_SampleSheet.csv) | CP2 |
| [251127_A01229_0637_AHGLV2DRX7_SampleSheet.csv](data/samplesheets/valid/251127_A01229_0637_AHGLV2DRX7_SampleSheet.csv) | OKD |