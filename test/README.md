# Test Suite

Tests for this module can be found in the [test_samplesheet_validator script](test_samplesheet_validator.py). These
have been written to cover testing all the functions in this package.

## Fixtures

Tests fixtures have been created which are passed into the test functions in order to test the functions in
[samplesheet_validator.py](../samplesheet_validator/samplesheet_validator.py). These test fixtures cover both invalid
and valid SampleSheets, and those that are invalid cover the various different ways in which a sample sheet can be
invalid.


### Test Samplesheets

#### [Invalid Samplesheets](data/samplesheets/invalid)

| Name | Why is it invalid? |
| ---- | ------------------ |
| [21aA08_A01229_0040_AHKGTFDRXY_SampleSheet.csv](data/samplesheets/invalid/21aA08_A01229_0040_AHKGTFDRXY_SampleSheet.csv) | Empty, Invalid date |
|[21108_A01229_0040_AHKGTFDRXY_SampleSheet.csv](data/samplesheets/invalid/21108_A01229_0040_AHKGTFDRXY_SampleSheet.csv) | None | Invalid date |
| [210917_NB551068_0409_ABCDEFGJIK_SampleSheet.csv](data/samplesheets/invalid/210917_NB551068_0409_ABCDEFGJIK_SampleSheet.csv) | Wrong naming format of at least one sample names |
| [210917_NB551068_9876_AH3YNFAFX3_SampleSheet.csv](data/samplesheets/invalid/210917_NB551068_9876_AH3YNFAFX3_SampleSheet.csv) | Invalid sample count for at least one sample name |
| [211008_1229_0040_AHKGTFDRXY_SampleSheet.csv](data/samplesheets/invalid/211008_1229_0040_AHKGTFDRXY_SampleSheet.csv) | Empty, invalid sequencer ID |
| [211008_A01229_0_AHKGTFDRXY_SampleSheet.csv](data/samplesheets/invalid/211008_A01229_0_AHKGTFDRXY_SampleSheet.csv) | Empty, invalid autoincrementing_number |
| [211008_A01229_0040_1AHK£lRXY_SampleSheet.csv](data/samplesheets/invalid/211008_A01229_0040_1AHK£lRXY_SampleSheet.csv) | Empty, invalid flow cell ID|
| [211008_A01229_0040_AHKGTFDRXY_samplesheet.csv](data/samplesheets/invalid/211008_A01229_0040_AHKGTFDRXY_samplesheet.csv) | Empty, with invalid 'SampleSheet' string |
| [211008_A01229_AHKGTFDRXY_SampleSheet.abc](data/samplesheets/invalid/211008_A01229_AHKGTFDRXY_SampleSheet.abc) | Empty, wrong file extension |
| [211008_A01229_AHKGTFDRXY_SampleSheet.csv](data/samplesheets/invalid/211008_A01229_AHKGTFDRXY_SampleSheet.csv) | Empty, wrong naming format |
| [220413_A01229_0032_AHKGTFDRXY_SampleSheet.csv](data/samplesheets/invalid/220413_A01229_0032_AHKGTFDRXY_SampleSheet.csv) | Empty with valid name |
| [220506_NB551068_0409_AH3YNFAFX3_SampleSheet.csv](data/samplesheets/invalid/220506_NB551068_0409_AH3YNFAFX3_SampleSheet.csv) | Invalid contents - invalid sex |
| [221021_A01229_0145_ZXYEORIUGI_SampleSheet.csv](data/samplesheets/invalid/221021_A01229_0145_ZXYEORIUGI_SampleSheet.csv) |  Invalid contents - invalid secondary identifier |
| [221021_A01229_0398_BHGGTHDMXY_SampleSheet.csv](data/samplesheets/invalid/221021_A01229_0398_BHGGTHDMXY_SampleSheet.csv) | |
| [221024_A01229_0146_EIROFPWYJL_SampleSheet.csv](data/samplesheets/invalid/221024_A01229_0146_EIROFPWYJL_SampleSheet.csv) | |
| [221024_A01229_0345_BERTYG2DRX2_SampleSheet.csv](data/samplesheets/invalid/221024_A01229_0345_BERTYG2DRX2_SampleSheet.csv) | |
| [221024_A01229_3746_BERIOG2DRX2_SampleSheet.csv](data/samplesheets/invalid/221024_A01229_3746_BERIOG2DRX2_SampleSheet.csv) | |
| [230309_E02631_4297_000000000-KRDLT_SampleSheet.csv](data/samplesheets/invalid/230309_E02631_4297_000000000-KRDLT_SampleSheet.csv) | Samplesheet containing multiple errors |
| [230309_M02631_0123_000000000-ABCDE_SampleSheet.csv](data/samplesheets/invalid/230309_M02631_0123_000000000-ABCDE_SampleSheet.csv) | Invalid contents - non matching sample names |
| [230309_M02631_0123_000000000-KRDLT_SampleSheet.csv](data/samplesheets/invalid/230309_M02631_0123_000000000-KRDLT_SampleSheet.csv) | Invalid contents - invalid headers |
| [230309_M02631_0275_000000000-ERTGL_SampleSheet.csv](data/samplesheets/invalid/230309_M02631_0275_000000000-ERTGL_SampleSheet.csv) | Invalid contents - invalid initials |
| [230309_M02631_0345_000000000-KRDLT_SampleSheet.csv](data/samplesheets/invalid/230309_M02631_0345_000000000-KRDLT_SampleSheet.csv) | Invalid contents - specimen/DNA number invalid |
| [230309_M02631_4567_000000000-KRDLT_SampleSheet.csv](data/samplesheets/invalid/230309_M02631_4567_000000000-KRDLT_SampleSheet.csv) | Invalid contents - invalid panel name |
| [231012_M02631_1234_000000000-LBGMH_SampleSheet.csv](data/samplesheets/invalid/231012_M02631_1234_000000000-LBGMH_SampleSheet.csv) | Invalid contents - Not enough identifiers in sample name |
| [231201_NB552085_0945_AHVNWYERYU_SampleSheet.csv](data/samplesheets/invalid/231201_NB552085_0945_AHVNWYERYU_SampleSheet.csv) | Invalid contents - invalid panel number |
| [2110915_M02353_0632_000000000-K242J_SampleSheet.csv](data/samplesheets/invalid/2110915_M02353_0632_000000000-K242J_SampleSheet.csv) | Invalid date |

#### [Valid Samplesheets](data/samplesheets/valid)
* [210917_NB551068_0409_AH3YNFAFX3_SampleSheet.csv](data/samplesheets/valid/210917_NB551068_0409_AH3YNFAFX3_SampleSheet.csv)
* [221021_A01229_0145_BHGGTHDMXY_SampleSheet.csv](data/samplesheets/valid/221021_A01229_0145_BHGGTHDMXY_SampleSheet.csv)
* [221024_A01229_0146_BHKGG2DRX2_SampleSheet.csv](data/samplesheets/valid/221024_A01229_0146_BHKGG2DRX2_SampleSheet.csv)
* [230309_M02631_0275_000000000-KRDLT_SampleSheet.csv](data/samplesheets/valid/230309_M02631_0275_000000000-KRDLT_SampleSheet.csv)
* [231012_M02631_0285_000000000-LBGMH_SampleSheet.csv](data/samplesheets/valid/231012_M02631_0285_000000000-LBGMH_SampleSheet.csv)
* [231116_NB551068_0551_AHLCYNAFX5_SampleSheet.csv](data/samplesheets/valid/231116_NB551068_0551_AHLCYNAFX5_SampleSheet.csv)
* [231201_NB552085_0291_AHVNWYAFX5_SampleSheet.csv](data/samplesheets/valid/231201_NB552085_0291_AHVNWYAFX5_SampleSheet.csv)