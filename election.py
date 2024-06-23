{"payload":{"allShortcutsEnabled":true,"fileTree":{"":{"items":[{"name":".idea","path":".idea","contentType":"directory"},{"name":".gitattributes","path":".gitattributes","contentType":"file"},{"name":"README.md","path":"README.md","contentType":"file"},{"name":"election.py","path":"election.py","contentType":"file"}],"totalCount":4}},"fileTreeProcessingTime":4.284141,"foldersToFetch":[],"repo":{"id":614894188,"defaultBranch":"main","name":"PythonScripts","ownerLogin":"DeCreed001","currentUserCanPush":true,"isFork":false,"isEmpty":false,"createdAt":"2023-03-16T15:30:38.000+01:00","ownerAvatar":"https://avatars.githubusercontent.com/u/64212945?v=4","public":true,"private":false,"isOrgOwned":false},"symbolsExpanded":false,"treeExpanded":true,"refInfo":{"name":"main","listCacheKey":"v0:1678977043.138077","canEdit":true,"refType":"branch","currentOid":"ef113a6fe9097331cdaa352b2927c84715844dde"},"path":"election.py","currentUser":{"id":64212945,"login":"DeCreed001","userEmail":"techbasengr@gmail.com"},"blob":{"rawLines":["import random","","# Generate random candidate data","PARTIES = ['Party A', 'Party B', 'Party C', 'Party D', 'Party E']","CANDIDATE_TYPES = {","    'Presidential Candidates': 3,","    'Senatorial Candidates': 3,","    'House of Representatives Candidates': 3,","    'Governorship Candidates': 3,","    'House of Assembly Candidates': 3","}","candidates = {}","for ctype, num in CANDIDATE_TYPES.items():","    candidates[ctype] = [(f\"{ctype[:-1]} {i}\", random.choice(PARTIES))","                         for i in range(1, num+1)]","","# Prompt user to insert Permanent Voters Card","print(\"Please insert your Permanent Voters Card.\")","","# Prompt user to select language","LANGUAGES = ['English', 'Yoruba', 'Igbo', 'Hausa']","selected_language = input(","    f\"Please select your language: {', '.join(LANGUAGES)}\\n\")","","# Display candidates and their parties for user to choose","for ctype, cands in candidates.items():","    print(f\"{ctype}:\")","    for i, candidate in enumerate(cands):","        print(f\"{i+1}. {candidate[0]} - {candidate[1]}\")","    selected_candidate = input(","        f\"Please select your preferred {ctype[:-1]} (1-3): \")","","# Eject Permanent Voters Card","print(\"\\nThank you for voting. Your Permanent Voters Card is now ejected.\")","","# Log votes in Management site","voters_card_number = input(\"\\nPlease enter your Voters Card Number: \")","print(","    f\"\\nYour vote has been recorded. To view the election results, please visit the Management site and enter your Voters Card Number: {voters_card_number}\")"],"stylingDirectives":[[{"start":0,"end":6,"cssClass":"pl-k"},{"start":7,"end":13,"cssClass":"pl-s1"}],[],[{"start":0,"end":32,"cssClass":"pl-c"}],[{"start":0,"end":7,"cssClass":"pl-v"},{"start":8,"end":9,"cssClass":"pl-c1"},{"start":11,"end":20,"cssClass":"pl-s"},{"start":22,"end":31,"cssClass":"pl-s"},{"start":33,"end":42,"cssClass":"pl-s"},{"start":44,"end":53,"cssClass":"pl-s"},{"start":55,"end":64,"cssClass":"pl-s"}],[{"start":0,"end":15,"cssClass":"pl-v"},{"start":16,"end":17,"cssClass":"pl-c1"}],[{"start":4,"end":29,"cssClass":"pl-s"},{"start":31,"end":32,"cssClass":"pl-c1"}],[{"start":4,"end":27,"cssClass":"pl-s"},{"start":29,"end":30,"cssClass":"pl-c1"}],[{"start":4,"end":41,"cssClass":"pl-s"},{"start":43,"end":44,"cssClass":"pl-c1"}],[{"start":4,"end":29,"cssClass":"pl-s"},{"start":31,"end":32,"cssClass":"pl-c1"}],[{"start":4,"end":34,"cssClass":"pl-s"},{"start":36,"end":37,"cssClass":"pl-c1"}],[],[{"start":0,"end":10,"cssClass":"pl-s1"},{"start":11,"end":12,"cssClass":"pl-c1"}],[{"start":0,"end":3,"cssClass":"pl-k"},{"start":4,"end":9,"cssClass":"pl-s1"},{"start":11,"end":14,"cssClass":"pl-s1"},{"start":15,"end":17,"cssClass":"pl-c1"},{"start":18,"end":33,"cssClass":"pl-v"},{"start":34,"end":39,"cssClass":"pl-en"}],[{"start":4,"end":14,"cssClass":"pl-s1"},{"start":15,"end":20,"cssClass":"pl-s1"},{"start":22,"end":23,"cssClass":"pl-c1"},{"start":26,"end":45,"cssClass":"pl-s"},{"start":28,"end":40,"cssClass":"pl-s1"},{"start":28,"end":29,"cssClass":"pl-kos"},{"start":29,"end":34,"cssClass":"pl-s1"},{"start":36,"end":37,"cssClass":"pl-c1"},{"start":37,"end":38,"cssClass":"pl-c1"},{"start":39,"end":40,"cssClass":"pl-kos"},{"start":41,"end":44,"cssClass":"pl-s1"},{"start":41,"end":42,"cssClass":"pl-kos"},{"start":42,"end":43,"cssClass":"pl-s1"},{"start":43,"end":44,"cssClass":"pl-kos"},{"start":47,"end":53,"cssClass":"pl-s1"},{"start":54,"end":60,"cssClass":"pl-en"},{"start":61,"end":68,"cssClass":"pl-v"}],[{"start":25,"end":28,"cssClass":"pl-k"},{"start":29,"end":30,"cssClass":"pl-s1"},{"start":31,"end":33,"cssClass":"pl-c1"},{"start":34,"end":39,"cssClass":"pl-en"},{"start":40,"end":41,"cssClass":"pl-c1"},{"start":43,"end":46,"cssClass":"pl-s1"},{"start":46,"end":47,"cssClass":"pl-c1"},{"start":47,"end":48,"cssClass":"pl-c1"}],[],[{"start":0,"end":45,"cssClass":"pl-c"}],[{"start":0,"end":5,"cssClass":"pl-en"},{"start":6,"end":49,"cssClass":"pl-s"}],[],[{"start":0,"end":32,"cssClass":"pl-c"}],[{"start":0,"end":9,"cssClass":"pl-v"},{"start":10,"end":11,"cssClass":"pl-c1"},{"start":13,"end":22,"cssClass":"pl-s"},{"start":24,"end":32,"cssClass":"pl-s"},{"start":34,"end":40,"cssClass":"pl-s"},{"start":42,"end":49,"cssClass":"pl-s"}],[{"start":0,"end":17,"cssClass":"pl-s1"},{"start":18,"end":19,"cssClass":"pl-c1"},{"start":20,"end":25,"cssClass":"pl-en"}],[{"start":4,"end":60,"cssClass":"pl-s"},{"start":35,"end":57,"cssClass":"pl-s1"},{"start":35,"end":36,"cssClass":"pl-kos"},{"start":36,"end":40,"cssClass":"pl-s"},{"start":41,"end":45,"cssClass":"pl-en"},{"start":46,"end":55,"cssClass":"pl-v"},{"start":56,"end":57,"cssClass":"pl-kos"},{"start":57,"end":59,"cssClass":"pl-cce"}],[],[{"start":0,"end":57,"cssClass":"pl-c"}],[{"start":0,"end":3,"cssClass":"pl-k"},{"start":4,"end":9,"cssClass":"pl-s1"},{"start":11,"end":16,"cssClass":"pl-s1"},{"start":17,"end":19,"cssClass":"pl-c1"},{"start":20,"end":30,"cssClass":"pl-s1"},{"start":31,"end":36,"cssClass":"pl-en"}],[{"start":4,"end":9,"cssClass":"pl-en"},{"start":10,"end":21,"cssClass":"pl-s"},{"start":12,"end":19,"cssClass":"pl-s1"},{"start":12,"end":13,"cssClass":"pl-kos"},{"start":13,"end":18,"cssClass":"pl-s1"},{"start":18,"end":19,"cssClass":"pl-kos"}],[{"start":4,"end":7,"cssClass":"pl-k"},{"start":8,"end":9,"cssClass":"pl-s1"},{"start":11,"end":20,"cssClass":"pl-s1"},{"start":21,"end":23,"cssClass":"pl-c1"},{"start":24,"end":33,"cssClass":"pl-en"},{"start":34,"end":39,"cssClass":"pl-s1"}],[{"start":8,"end":13,"cssClass":"pl-en"},{"start":14,"end":55,"cssClass":"pl-s"},{"start":16,"end":21,"cssClass":"pl-s1"},{"start":16,"end":17,"cssClass":"pl-kos"},{"start":17,"end":18,"cssClass":"pl-s1"},{"start":18,"end":19,"cssClass":"pl-c1"},{"start":19,"end":20,"cssClass":"pl-c1"},{"start":20,"end":21,"cssClass":"pl-kos"},{"start":23,"end":37,"cssClass":"pl-s1"},{"start":23,"end":24,"cssClass":"pl-kos"},{"start":24,"end":33,"cssClass":"pl-s1"},{"start":34,"end":35,"cssClass":"pl-c1"},{"start":36,"end":37,"cssClass":"pl-kos"},{"start":40,"end":54,"cssClass":"pl-s1"},{"start":40,"end":41,"cssClass":"pl-kos"},{"start":41,"end":50,"cssClass":"pl-s1"},{"start":51,"end":52,"cssClass":"pl-c1"},{"start":53,"end":54,"cssClass":"pl-kos"}],[{"start":4,"end":22,"cssClass":"pl-s1"},{"start":23,"end":24,"cssClass":"pl-c1"},{"start":25,"end":30,"cssClass":"pl-en"}],[{"start":8,"end":60,"cssClass":"pl-s"},{"start":39,"end":51,"cssClass":"pl-s1"},{"start":39,"end":40,"cssClass":"pl-kos"},{"start":40,"end":45,"cssClass":"pl-s1"},{"start":47,"end":48,"cssClass":"pl-c1"},{"start":48,"end":49,"cssClass":"pl-c1"},{"start":50,"end":51,"cssClass":"pl-kos"}],[],[{"start":0,"end":29,"cssClass":"pl-c"}],[{"start":0,"end":5,"cssClass":"pl-en"},{"start":6,"end":74,"cssClass":"pl-s"},{"start":7,"end":9,"cssClass":"pl-cce"}],[],[{"start":0,"end":30,"cssClass":"pl-c"}],[{"start":0,"end":18,"cssClass":"pl-s1"},{"start":19,"end":20,"cssClass":"pl-c1"},{"start":21,"end":26,"cssClass":"pl-en"},{"start":27,"end":69,"cssClass":"pl-s"},{"start":28,"end":30,"cssClass":"pl-cce"}],[{"start":0,"end":5,"cssClass":"pl-en"}],[{"start":4,"end":156,"cssClass":"pl-s"},{"start":6,"end":8,"cssClass":"pl-cce"},{"start":135,"end":155,"cssClass":"pl-s1"},{"start":135,"end":136,"cssClass":"pl-kos"},{"start":136,"end":154,"cssClass":"pl-s1"},{"start":154,"end":155,"cssClass":"pl-kos"}]],"colorizedLines":null,"csv":null,"csvError":null,"dependabotInfo":{"showConfigurationBanner":null,"configFilePath":null,"networkDependabotPath":"/DeCreed001/PythonScripts/network/updates","dismissConfigurationNoticePath":"/settings/dismiss-notice/dependabot_configuration_notice","configurationNoticeDismissed":false},"displayName":"election.py","displayUrl":"https://github.com/DeCreed001/PythonScripts/blob/main/election.py?raw=true","headerInfo":{"blobSize":"1.43 KB","deleteTooltip":"Delete this file","editTooltip":"Edit this file","ghDesktopPath":"x-github-client://openRepo/https://github.com/DeCreed001/PythonScripts?branch=main&filepath=election.py","isGitLfs":false,"onBranch":true,"shortPath":"ee332bb","siteNavLoginPath":"/login?return_to=https%3A%2F%2Fgithub.com%2FDeCreed001%2FPythonScripts%2Fblob%2Fmain%2Felection.py","isCSV":false,"isRichtext":false,"toc":null,"lineInfo":{"truncatedLoc":"39","truncatedSloc":"33"},"mode":"file"},"image":false,"isCodeownersFile":null,"isPlain":false,"isValidLegacyIssueTemplate":false,"issueTemplate":null,"discussionTemplate":null,"language":"Python","languageID":303,"large":false,"planSupportInfo":{"repoIsFork":null,"repoOwnedByCurrentUser":null,"requestFullPath":"/DeCreed001/PythonScripts/blob/main/election.py","showFreeOrgGatedFeatureMessage":null,"showPlanSupportBanner":null,"upgradeDataAttributes":null,"upgradePath":null},"publishBannersInfo":{"dismissActionNoticePath":"/settings/dismiss-notice/publish_action_from_dockerfile","releasePath":"/DeCreed001/PythonScripts/releases/new?marketplace=true","showPublishActionBanner":false},"rawBlobUrl":"https://github.com/DeCreed001/PythonScripts/raw/main/election.py","renderImageOrRaw":false,"richText":null,"renderedFileInfo":null,"shortPath":null,"symbolsEnabled":true,"tabSize":8,"topBannersInfo":{"overridingGlobalFundingFile":false,"globalPreferredFundingPath":null,"showInvalidCitationWarning":false,"citationHelpUrl":"https://docs.github.com/github/creating-cloning-and-archiving-repositories/creating-a-repository-on-github/about-citation-files","actionsOnboardingTip":null},"truncated":false,"viewable":true,"workflowRedirectUrl":null,"symbols":{"timed_out":false,"not_analyzed":false,"symbols":[{"name":"PARTIES","kind":"constant","ident_start":48,"ident_end":55,"extent_start":48,"extent_end":113,"fully_qualified_name":"PARTIES","ident_utf16":{"start":{"line_number":3,"utf16_col":0},"end":{"line_number":3,"utf16_col":7}},"extent_utf16":{"start":{"line_number":3,"utf16_col":0},"end":{"line_number":3,"utf16_col":65}}},{"name":"CANDIDATE_TYPES","kind":"constant","ident_start":114,"ident_end":129,"extent_start":114,"extent_end":319,"fully_qualified_name":"CANDIDATE_TYPES","ident_utf16":{"start":{"line_number":4,"utf16_col":0},"end":{"line_number":4,"utf16_col":15}},"extent_utf16":{"start":{"line_number":4,"utf16_col":0},"end":{"line_number":10,"utf16_col":1}}},{"name":"candidates","kind":"constant","ident_start":320,"ident_end":330,"extent_start":320,"extent_end":335,"fully_qualified_name":"candidates","ident_utf16":{"start":{"line_number":11,"utf16_col":0},"end":{"line_number":11,"utf16_col":10}},"extent_utf16":{"start":{"line_number":11,"utf16_col":0},"end":{"line_number":11,"utf16_col":15}}},{"name":"LANGUAGES","kind":"constant","ident_start":633,"ident_end":642,"extent_start":633,"extent_end":683,"fully_qualified_name":"LANGUAGES","ident_utf16":{"start":{"line_number":20,"utf16_col":0},"end":{"line_number":20,"utf16_col":9}},"extent_utf16":{"start":{"line_number":20,"utf16_col":0},"end":{"line_number":20,"utf16_col":50}}},{"name":"selected_language","kind":"constant","ident_start":684,"ident_end":701,"extent_start":684,"extent_end":772,"fully_qualified_name":"selected_language","ident_utf16":{"start":{"line_number":21,"utf16_col":0},"end":{"line_number":21,"utf16_col":17}},"extent_utf16":{"start":{"line_number":21,"utf16_col":0},"end":{"line_number":22,"utf16_col":61}}},{"name":"voters_card_number","kind":"constant","ident_start":1227,"ident_end":1245,"extent_start":1227,"extent_end":1297,"fully_qualified_name":"voters_card_number","ident_utf16":{"start":{"line_number":36,"utf16_col":0},"end":{"line_number":36,"utf16_col":18}},"extent_utf16":{"start":{"line_number":36,"utf16_col":0},"end":{"line_number":36,"utf16_col":70}}}]}},"copilotInfo":{"documentationUrl":"https://docs.github.com/copilot/overview-of-github-copilot/about-github-copilot-for-individuals","notices":{"codeViewPopover":{"dismissed":false,"dismissPath":"/settings/dismiss-notice/code_view_copilot_popover"}},"userAccess":{"hasSubscriptionEnded":false,"orgHasCFBAccess":false,"userHasCFIAccess":false,"userHasOrgs":false,"userIsOrgAdmin":false,"userIsOrgMember":false,"business":null,"featureRequestInfo":null}},"copilotAccessAllowed":false,"csrf_tokens":{"/DeCreed001/PythonScripts/branches":{"post":"wFDKWkeq5cPxAVm--V_jsdy5h_nadDl8ItgaeVeciOp8hElETKLigtbL36qXXbu_xTy1bmRQNpExcaqa8X2iyw"},"/repos/preferences":{"post":"ZhAhFs1zldrzRTcMIwnBq8SDOEXgQ78N0hIRuyjUzIx9Az6sAvOAfcprTpcwX7ZmKVGiFwbWx2Gr_ZXc1Q0rgw"}}},"title":"PythonScripts/election.py at main · DeCreed001/PythonScripts"}