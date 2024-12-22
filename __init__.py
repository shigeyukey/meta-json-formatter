from aqt.addons import AddonManager, Any
from anki.hooks import wrap
import json

INDENT_NUMBER = 4
# You can change the number of indents for json.

WRAP_POS = "around"
# "around" No call to the original func. If something problems occurs do not save config.
# "after" Runs after the original func. If there is an error it can be save config, but it writes twice so performance is a bit slower.

if WRAP_POS == "after":
    def writeAddonMeta_wrapper(self:AddonManager, module: str, meta: dict[str, Any]) -> None:
        path = self._addonMetaPath(module)
        with open(path, "w", encoding="utf8") as f:
            json.dump(meta, f, indent=INDENT_NUMBER)
else :
    def writeAddonMeta_wrapper(self:AddonManager, module: str, meta: dict[str, Any], _old) -> None:
        path = self._addonMetaPath(module)
        with open(path, "w", encoding="utf8") as f:
            json.dump(meta, f, indent=INDENT_NUMBER)

if hasattr(AddonManager, "writeAddonMeta"):
    AddonManager.writeAddonMeta = wrap(AddonManager.writeAddonMeta, writeAddonMeta_wrapper, WRAP_POS)
