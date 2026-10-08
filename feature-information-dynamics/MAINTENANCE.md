# Project page maintenance

`index.html` is the only project-page source. It contains English and Chinese prose,
shared measured display data, interaction and language controls. Do not regenerate
it from a template or copy in the code repository.

Preview this repository directly with a local HTTP server. Generate README GIFs
from this same page. Verify both languages, formula rendering, selected sample and
SNR preservation, mobile layout and citation before publication.

The code repository owns its notebook and README. Refresh the downloadable notebook
asset from that repository explicitly. `tools/prepare_feature_information_figures.py`
accepts the paper directory and updates this site's figure assets.

Legacy figure/asset provenance is retained under `provenance/`; it is historical,
not a current asset-integrity manifest. New output must record its own provenance.
