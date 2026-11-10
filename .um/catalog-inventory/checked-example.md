> **Saved-check reclassification — not a new workflow run.** Existing link-check logs were evaluated with the updated classifier. No model calls or fresh network checks were made. The saved checks still pass: every changed-row destination succeeded.

# One-entry integration example

Saved initial research was reused. Prior discussion collection, Opus history review, patch validation and report rendering ran through the current production code. This is not a full catalog run.

# Catalog review

**1 ready for review · 0 held**

1 checked · 0 unchanged · 1 saved assessment reused · 0 source checks unavailable

<h2>Ansible Google Groups — Ready for maintainer review</h2>

```diff
--- a/README.md
+++ b/README.md
@@ -62,7 +62,7 @@
 
 # Community
 
-- [Ansible Google Groups](https://groups.google.com/forum/#!forum/ansible-project) - Ansible's mailing list and forum!
+- [Ansible Forum](https://forum.ansible.com/) - The official Ansible community forum, which replaced the now read-only Ansible Google Groups mailing lists.
 - [IRC Ansible](https://docs.ansible.com/ansible/community.html#irc-channel) - Ansible IRC Channels.
 - [Chef Community](https://community.chef.io/) - The complete offical list of Chef Community resources.
 - [Infrahub Community](https://discord.gg/opsmill) - Discord server for the Infrahub community to discuss infrastructure automation, ask questions, and connect with other users.
```

<details>
<summary>Evidence and checks</summary>

<p>Ansible&#x27;s own announcement says the Ansible Google Groups (including ansible-project) were made read-only on 2024-09-17, and that all support moved to the Ansible Forum at forum.ansible.com. The group&#x27;s banner now says it has migrated to forum.ansible.com. The listed link is now an archive, not Ansible&#x27;s mailing list and forum, so the documented official successor is the Ansible Forum.</p>

<p>https://groups.google.com/g/ansible-project — Group header says: &#x27;The Ansible Google Groups has migrated to forum.ansible.com.&#x27; The pinned post by Gundalow Barker (9/17/24) says: &#x27;The Ansible Google Groups are now readonly.&#x27;</p>

<p>https://forum.ansible.com/t/important-ansible-google-group-moving-to-ansible-forum/38853 — Official migration plan: new posts move to the forum, then the Google group goes read-only and all support is handled on the forum. A follow-up on 2024-09-17 by the Ansible Community Engineering Manager confirms the groups are read-only.</p>

<p>https://forum.ansible.com/ — The Ansible Community forum (Discourse) is live, with Get Help, Project Discussions, Events and News categories and thousands of topics.</p>

<p>https://docs.ansible.com/projects/ansible/latest/community/communication.html — Official docs name the Forum as &#x27;our default communication platform&#x27;.</p>

<p>Caveats: Entry 66 (IRC) also points users to the Forum/Matrix. The maintainer may want to avoid listing the forum twice.</p>

<p>clear: The search finished (complete=true) with no errors and found no records. It ran 8 queries across both networktocode/awesome-network-automation and bromanko/awesome-network-automation. They searched titles, bodies and comments for the current entry name (&quot;Ansible Google Groups&quot;), the current URL (https://groups.google.com/forum/#!forum/ansible-project), the proposed URL (https://forum.ansible.com/) and the proposed name (&quot;Ansible Forum&quot;). Within those queries, there is no open PR proposing the same replacement, no maintainer rejection and no merged change, so nothing overlaps. These queries are the only search done; nothing wider was checked. One editorial point remains from the proposal: entry 66 (IRC) also points users to the Forum, so the maintainer may want to avoid listing the forum twice. That is not a competing correction. Exact patch and link checks passed; unrelated existing link failures are listed separately.</p>

</details>

<details>
<summary>Saved review baseline</summary>

0 new completed reviews · 1 pending.

To retain completed reviews, review and commit the bundled `baseline.json` as `.um/freshness/baseline.json`.

</details>

<details>
<summary>Full research and run details</summary>

# Freshness research

Advisory only; every suggested change requires maintainer review.
No list edits, PRs, comments, or reviews were submitted.

Catalog revision: `ed5fd3a7df95bb3d72fddbca83aca7a88bed55f2`
Scope: one saved-research entry; not a full catalog run
Catalog recheck: unchanged

Sources below are agent-reported observations, not independent verification.

## Entry 65

<pre>Ansible Google Groups

Ansible&#x27;s own announcement says the Ansible Google Groups (including ansible-project) were made read-only on 2024-09-17, and that all support moved to the Ansible Forum at forum.ansible.com. The group&#x27;s banner now says it has migrated to forum.ansible.com. The listed link is now an archive, not Ansible&#x27;s mailing list and forum, so the documented official successor is the Ansible Forum.

https://groups.google.com/g/ansible-project
Group header says: &#x27;The Ansible Google Groups has migrated to forum.ansible.com.&#x27; The pinned post by Gundalow Barker (9/17/24) says: &#x27;The Ansible Google Groups are now readonly.&#x27;
https://forum.ansible.com/t/important-ansible-google-group-moving-to-ansible-forum/38853
Official migration plan: new posts move to the forum, then the Google group goes read-only and all support is handled on the forum. A follow-up on 2024-09-17 by the Ansible Community Engineering Manager confirms the groups are read-only.
https://forum.ansible.com/
The Ansible Community forum (Discourse) is live, with Get Help, Project Discussions, Events and News categories and thousands of topics.
https://docs.ansible.com/projects/ansible/latest/community/communication.html
Official docs name the Forum as &#x27;our default communication platform&#x27;.

Blocking uncertainties:
None reported.

Informational caveats:
Entry 66 (IRC) also points users to the Forum/Matrix. The maintainer may want to avoid listing the forum twice.

Recommendation: replace
Proposed name: Ansible Forum
Proposed URL: https://forum.ansible.com/
Proposed description: The official Ansible community forum, which replaced the now read-only Ansible Google Groups mailing lists.</pre>


</details>

Proposals only; no catalog edits or PRs submitted. Full records and checked patches are in the run artifacts.
