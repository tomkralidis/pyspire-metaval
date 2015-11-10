
# INSPIRE Metadata Validation Service Python wrapper

## Overview

Simple Pythonic Wrapper to INSPIRE Metadata Validation Service

## Metadata Records

http://geodata.gov.gr/csw?service=CSW&version=2.0.2&request=GetRecordById&id=0f5b2fe2-eec2-4f46-89a6-1a7b390735b8&outputschema=http://www.isotc211.org/2005/gmd&elementsetname=full

## Invocation

```bash
# test against a locally saved copy of http://geodata.gov.gr/csw?service=CSW&version=2.0.2&request=GetRecordById&id=0f5b2fe2-eec2-4f46-89a6-1a7b390735b8&outputschema=http://www.isotc211.org/2005/gmd&elementsetname=full
python inspire-metadata-validate.py inspire-good.xml | json_pp > inspire-good-result.json

# test against a locally saved copy with (errors added) of http://geodata.gov.gr/csw?service=CSW&version=2.0.2&request=GetRecordById&id=0f5b2fe2-eec2-4f46-89a6-1a7b390735b8&outputschema=http://www.isotc211.org/2005/gmd&elementsetname=full
python inspire-metadata-validate.py inspire-bad.xml | json_pp > inspire-bad-result.json

# show differences between good and bad
diff inspire-good.xml inspire-bad.xml
280a281
>   <something_else/>
```

