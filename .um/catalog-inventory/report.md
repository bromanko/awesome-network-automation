# Catalog review inventory

**104 proposed changes · 25 uncertain · 56 unresolved keeps**

329 entries researched. 144 saved reviews for recurring runs.

Research recommendations from the initial Opus review. The full set has not passed prior-discussion or patch validation. Proposed diffs are previews, not approved patches. Nothing was applied or submitted.

Catalog: `2a170d9f6ba7e9b4e16ec6639913c4edcecda8d8` · README SHA-256: `3da110354452828e8961960284fc61a1c27ab10053f3e5c22794f3caac425bf1`

## Proposed changes

<h3>Ansible Google Groups — replace</h3>

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
<summary>Evidence and limitations</summary>

<p>Ansible&#x27;s own announcement says the Ansible Google Groups (including ansible-project) were made read-only on 2024-09-17, and that all support moved to the Ansible Forum at forum.ansible.com. The group&#x27;s banner now says it has migrated to forum.ansible.com. The listed link is now an archive, not Ansible&#x27;s mailing list and forum, so the documented official successor is the Ansible Forum.</p>

<p>https://groups.google.com/g/ansible-project — Group header says: &#x27;The Ansible Google Groups has migrated to forum.ansible.com.&#x27; The pinned post by Gundalow Barker (9/17/24) says: &#x27;The Ansible Google Groups are now readonly.&#x27;</p>

<p>https://forum.ansible.com/t/important-ansible-google-group-moving-to-ansible-forum/38853 — Official migration plan: new posts move to the forum, then the Google group goes read-only and all support is handled on the forum. A follow-up on 2024-09-17 by the Ansible Community Engineering Manager confirms the groups are read-only.</p>

<p>https://forum.ansible.com/ — The Ansible Community forum (Discourse) is live, with Get Help, Project Discussions, Events and News categories and thousands of topics.</p>

<p>https://docs.ansible.com/projects/ansible/latest/community/communication.html — Official docs name the Forum as &#x27;our default communication platform&#x27;.</p>

<p>Caveats: Entry 66 (IRC) also points users to the Forum/Matrix. The maintainer may want to avoid listing the forum twice.</p>

<p>Independent source check: Official migration announcement explicitly identifies the replacement forum and states the Google groups became read-only. This is a documented successor, not an archive-implies-irrelevance inference.</p>

<p>https://forum.ansible.com/t/important-ansible-google-group-moving-to-ansible-forum/38853 — Official announcement and September 17, 2024 follow-up confirm migration and read-only status.</p>

<p>https://docs.ansible.com/projects/ansible/latest/community/communication.html — Current docs recommend the Ansible Forum for community interactions.</p>

</details>

<h3>AWS Reinvent — update</h3>

<p>0 proposed change(s); 1 held for unresolved questions.</p>

<details>
<summary>Evidence and limitations</summary>

<p>reinvent.awsevents.com redirects to https://aws.amazon.com/events/reinvent/. That page now presents &#x27;AWS re:Invent 2026 | The Premier Cloud and AI Conference | Nov 30-Dec 4, Las Vegas&#x27;, with sessions, expo, livestream and community. The description quotes an old &#x27;re:Invent Central&#x27; sponsor-connection portal that no longer describes the destination. The URL and description should be corrected.</p>

<p>https://aws.amazon.com/events/reinvent/ — Final URL after redirect. Title: &#x27;AWS re:Invent 2026 | The Premier Cloud and AI Conference | Nov 30-Dec 4, Las Vegas&#x27;. Navigation: Agenda, Sessions, Experiences, Sponsors, Livestream, Event catalog, Expo. No &#x27;re:Invent Central&#x27; wording.</p>

<p>Blocking questions: The destination is now the main AWS re:Invent conference site, so replacing the old sponsor-portal description is justified. The proposed wording adds specific networking and infrastructure-automation coverage not established by its cited landing-page evidence; use a narrower conference description or add session evidence. Existing relevance is a curator decision, not grounds for automatic removal.</p>

<p>Caveats: Fit with network automation is indirect. re:Invent is a general cloud/AI conference that includes networking and infrastructure-automation sessions. Whether it stays is an editorial call that pre-dates this review.</p>

<p>Independent source check: The destination is now the main AWS re:Invent conference site, so replacing the old sponsor-portal description is justified. The proposed wording adds specific networking and infrastructure-automation coverage not established by its cited landing-page evidence; use a narrower conference description or add session evidence. Existing relevance is a curator decision, not grounds for automatic removal.</p>

<p>https://aws.amazon.com/events/reinvent/ — Main 2026 cloud/AI event with sessions, workshops, expo and livestream; landing-page evidence supports conference framing.</p>

</details>

<h3>Ansible Fest — update</h3>

```diff
--- a/README.md
+++ b/README.md
@@ -77,7 +77,7 @@
 # Events / Meetup
 
 - [AWS Reinvent](https://reinvent.awsevents.com/) - AWS re:Invent Central is designed to facilitate connections between sponsors and attendees.
-- [Ansible Fest](https://www.ansible.com/ansiblefest) - AnsibleFest is a day-long conference bringing together Ansible users, developers and industry partners to share best practices, case studies and Ansible news.
+- [Red Hat Summit and AnsibleFest](https://www.redhat.com/en/summit) - Red Hat's annual multi-day conference, held together with AnsibleFest, bringing together Ansible users, developers and partners to share automation best practices, case studies and news.
 - [Ansible NYC Meetup](https://www.meetup.com/Ansible-NYC/) - Local NYC Ansible user meetup.
 - [Chef Summits](https://www.chef.io/summits/) - Chef community summit schedule.
 - [London Network Automation Meetup](https://www.linkedin.com/company/london-network-automation-meetup/) - A community of network engineers, who have interest in the new buzz of network automation.
```

<details>
<summary>Evidence and limitations</summary>

<p>www.ansible.com/ansiblefest now redirects to https://www.redhat.com/en/summit. Red Hat runs AnsibleFest inside Red Hat Summit: &#x27;Red Hat Summit and AnsibleFest 2026, May 11-14, 2026&#x27; in Atlanta. The description&#x27;s &#x27;day-long conference&#x27; is no longer accurate. The name and URL should reflect the combined event.</p>

<p>https://www.redhat.com/en/blog/save-date-red-hat-summit-2026 — Official Red Hat blog: &#x27;Join us for Red Hat Summit and AnsibleFest 2026, May 11-14, 2026&#x27; in Atlanta, an annual event for customers, partners and open source community members.</p>

<p>https://www.redhat.com/en/summit — Destination of the ansible.com/ansiblefest redirect (HTTP 200). Page content is JS-rendered and AnsibleFest text was not in static HTML.</p>

<p>https://www.redhat.com/en/blog/definitive-automation-guide-red-hat-summit-2026-must-attend-red-hat-ansible-automation-platform-sessions-talks-and-labs — Official Red Hat automation session guide for Summit 2026, covering Ansible Automation Platform talks and labs (seen via search result).</p>

<p>Caveats: The redhat.com/en/summit page content is JS-rendered. AnsibleFest branding was confirmed through the official Red Hat blog, not the static landing page.; The combined event&#x27;s future branding may change year to year.</p>

<p>Independent source check: Official Red Hat announcement identifies the combined Summit/AnsibleFest event over four days, contradicting the catalog day-long description. The combined-event name and durable multi-day wording are supported.</p>

<p>https://www.redhat.com/en/blog/save-date-red-hat-summit-2026 — Red Hat announces Summit and AnsibleFest in Atlanta on May 11–14, 2026.</p>

</details>

<h3>Chef Summits — update</h3>

```diff
--- a/README.md
+++ b/README.md
@@ -79,7 +79,7 @@
 - [AWS Reinvent](https://reinvent.awsevents.com/) - AWS re:Invent Central is designed to facilitate connections between sponsors and attendees.
 - [Ansible Fest](https://www.ansible.com/ansiblefest) - AnsibleFest is a day-long conference bringing together Ansible users, developers and industry partners to share best practices, case studies and Ansible news.
 - [Ansible NYC Meetup](https://www.meetup.com/Ansible-NYC/) - Local NYC Ansible user meetup.
-- [Chef Summits](https://www.chef.io/summits/) - Chef community summit schedule.
+- [Chef Events](https://www.progress.com/events?filter=language%5Eenglish%7Cproduct%5Echef) - Progress Chef events schedule, including Chef roadshows and webinars.
 - [London Network Automation Meetup](https://www.linkedin.com/company/london-network-automation-meetup/) - A community of network engineers, who have interest in the new buzz of network automation.
 - [Minnesota Network User Group](https://www.meetup.com/mn-nug/) - Minnesota Network User Group, quarterly meetup of network users.
 - [NANOG](https://www.nanog.org) - North American Network Operators' Group with fair share of automation presentations/discussions.
```

<details>
<summary>Evidence and limitations</summary>

<p>chef.io/summits now 301-redirects to the official Progress events listing filtered to Chef (Progress owns Chef). Chef Community Summits are not advertised there. Current Chef events are Progress roadshows, e.g. &#x27;Chef Roadshow London 2026&#x27; (Oct 7, 2026). The description &#x27;Chef community summit schedule&#x27; no longer matches the destination. Updating the URL to the canonical redirect target and the wording to the Chef events schedule matches what is actually published.</p>

<p>https://www.progress.com/events?filter=language%5Eenglish%7Cproduct%5Echef — Final destination of the www.chef.io/summits redirect: the Progress Events listing with the product=Chef filter. Static HTML showed &#x27;All Upcoming Events … No items found&#x27; (the list may be JS-rendered).</p>

<p>https://www.progress.com/events/chef-roadshow-london-2026 — Official Progress event: &#x27;Chef Roadshow London 2026&#x27;, October 07, 2026, RAF Club London. Sessions on Chef 360, infrastructure automation and compliance.</p>

<p>https://www.chef.io/blog/chef-community-summits-seattle-london — The latest Chef Community Summits found were the 2018 Seattle and London events (seen via search result). This supports that the &#x27;summit&#x27; wording is historic.</p>

<p>Caveats: Fit with network automation is indirect (general config management). This pre-dates the review.; The filtered listing may show no upcoming events at times.</p>

<p>Independent source check: Independent HTTP fetch confirmed chef.io/summits redirects to Progress Events filtered for Chef. The official Chef roadshow and Chef community events/webinar links support broader event wording. Do not claim every historical summit was discontinued.</p>

<p>https://www.chef.io/summits/ — Redirects to https://www.progress.com/events?filter=language%5eenglish%7cproduct%5echef.</p>

<p>https://www.progress.com/events/chef-roadshow-london-2026 — Official Chef Roadshow event, October 7, 2026, with infrastructure-automation agenda.</p>

<p>https://community.chef.io/ — Official community page links Chef Events and webinar resources.</p>

</details>

<h3>Network to Coders Meetup — update</h3>

<p>0 proposed change(s); 1 held for unresolved questions.</p>

<details>
<summary>Evidence and limitations</summary>

<p>The Meetup group is live: &#x27;Network to Coders&#x27;, New York, 310 members, run by Network to Code (Jason Edelman). Its about text covers network automation, programmability and DevOps. The current description, &#x27;Maybe this can pressure NTC to finally setup an event for the 140+ NTC meetup members&#x27;, is outdated and incorrect. The group has held 4 events (Jan, Feb, Apr and Jun 2018) and has 310 members, not 140+. A neutral factual description is needed.</p>

<p>https://www.meetup.com/network-to-coders/ — &#x27;Network to Coders&#x27;, New York, NY, 310 members. About: &#x27;focused on automation, programmability, DevOps, and thinking differently about network operations… Target audience is network engineers&#x27;. 4 past events: Jan 10, 2018; Feb 7, 2018 (Vendor &amp; Platform Neutral Data Models with Ansible); Apr 30, 2018; Jun 20, 2018 (gRPC and OpenConfig). Organizer Jason Edelman. Links slack.networktocode.com.</p>

<p>Blocking questions: The group has four documented past events, so the request to finally arrange a first event is outdated and the proposed neutral description is supported. However 310/312 members does not contradict 140+; drop that incorrect rationale. Dormancy itself is not a removal reason.</p>

<p>Caveats: No events since June 2018 are listed. The group appears dormant, which does not by itself justify removal.</p>

<p>Independent source check: The group has four documented past events, so the request to finally arrange a first event is outdated and the proposed neutral description is supported. However 310/312 members does not contradict 140+; drop that incorrect rationale. Dormancy itself is not a removal reason.</p>

<p>https://www.meetup.com/network-to-coders/ — Lists four 2018 events, New York location, network-automation focus, and Network to Code sponsorship. Cached page member count was312, illustrating volatility.</p>

</details>

<h3>IRC Ansible — replace</h3>

```diff
--- a/README.md
+++ b/README.md
@@ -63,7 +63,7 @@
 # Community
 
 - [Ansible Google Groups](https://groups.google.com/forum/#!forum/ansible-project) - Ansible's mailing list and forum!
-- [IRC Ansible](https://docs.ansible.com/ansible/community.html#irc-channel) - Ansible IRC Channels.
+- [Ansible Matrix Chat](https://docs.ansible.com/projects/ansible/latest/community/communication.html#real-time-chat) - Ansible's official Matrix real-time chat rooms, which replaced the former IRC channels.
 - [Chef Community](https://community.chef.io/) - The complete offical list of Chef Community resources.
 - [Infrahub Community](https://discord.gg/opsmill) - Discord server for the Infrahub community to discuss infrastructure automation, ask questions, and connect with other users.
 - [Network Automation Forum](https://networkautomation.forum/) - A conference focused on Network Automation.
```

<details>
<summary>Evidence and limitations</summary>

<p>The listed URL (docs.ansible.com/ansible/community.html) now redirects to docs.ansible.com/projects/ansible/community.html, which returns 404. The current official communication page says: &#x27;IRC channels are no longer official communication channels. Use the Forum and Matrix instead.&#x27; It documents Matrix as the real-time chat platform, with rooms such as #social:ansible.com and #devel:ansible.com. The documented successor to the Ansible IRC channels is Ansible&#x27;s Matrix chat.</p>

<p>https://docs.ansible.com/projects/ansible/latest/community/communication.html — Official doc: &#x27;For real-time interactions, the Ansible community uses the Matrix protocol.&#x27; Note: &#x27;IRC channels are no longer official communication channels. Use the Forum and Matrix instead.&#x27; Has anchors #real-time-chat and #general-channels, with matrix.to links for #social:ansible.com and #devel:ansible.com.</p>

<p>https://docs.ansible.com/ansible/community.html — 301 → https://docs.ansible.com/projects/ansible/community.html, which returns HTTP 404.</p>

<p>Caveats: The Forum is the default platform. The Forum is suggested as the successor for entry 65, so Matrix is used here to avoid duplication.</p>

<p>Independent source check: Current Ansible documentation explicitly retires IRC as an official channel and names Forum and Matrix instead; the Matrix replacement is supported.</p>

<p>https://docs.ansible.com/projects/ansible/latest/community/communication.html — Documents Matrix real-time rooms and explicitly says IRC is no longer official.</p>

<p>Source snapshot incomplete; excluded from the saved baseline.</p>

</details>

<h3>SaltStack Community Slack  — replace</h3>

```diff
--- a/README.md
+++ b/README.md
@@ -72,7 +72,7 @@
 - [Salt Formulas](https://groups.google.com/forum/#!forum/salt-formulas) - The SaltStack formulas working group.
 - [Salt Networks](https://groups.google.com/forum/#!forum/salt-networks) - A centralized group for talking about network device automation with SaltStack.
 - [Salt Users](https://groups.google.com/forum/#!forum/salt-users) - The official forum of the Salt community.
-- [SaltStack Community Slack ](https://saltstackcommunity.slack.com/) - The official Slack of Saltstack Project.
+- [Salt Project Community Discord](https://discord.gg/J7b7EscrAs) - The official Discord server of the Salt Project community, which replaced the former SaltStack Community Slack.
 
 # Events / Meetup
 
```

<details>
<summary>Evidence and limitations</summary>

<p>Salt Project officially ended its Slack use on 2024-03-21 and moved the community to Discord. The Slack was read-only until the end of May 2024. The official site now links the &#x27;Salt Project Discord&#x27; (https://discord.gg/J7b7EscrAs), which resolves to the &#x27;Salt Project Community&#x27; guild. The listed Slack URL returns 403, and the old Heroku Slack invite app is gone.</p>

<p>https://saltproject.io/blog/goodbye-slack-hello-discord/ — &#x27;Effective immediately, March 21, 2024, Salt Project is ending our usage of Slack, and switching to Discord… virtually all Slack content has already been migrated… The Salt Project Slack workspace will remain live until the end of May 2024… READ ONLY.&#x27; Links https://discord.gg/J7b7EscrAs.</p>

<p>https://saltproject.io/community/ — Official Community navigation: Event Calendar, Working Groups, &#x27;Salt Project Discord&#x27; (https://discord.gg/J7b7EscrAs), Salt Project GitHub.</p>

<p>https://discord.com/api/v9/invites/J7b7EscrAs?with_counts=true — Invite resolves to guild &#x27;Salt Project Community&#x27;, about 1035 members, expires_at null.</p>

<p>https://saltstackcommunity.slack.com/ — HTTP 403. Separately, the old saltstackcommunity.herokuapp.com invite returns &#x27;No such app&#x27;.</p>

<p>Independent source check: Salt explicitly ended Slack use and moved to Discord. No inference from a 403 is required.</p>

<p>https://saltproject.io/blog/goodbye-slack-hello-discord/ — Official migration effective March 21, 2024, with community Discord invite and Slack read-only transition.</p>

<p>Source snapshot incomplete; excluded from the saved baseline.</p>

</details>

<h3>SaltStack NYC Meetup — remove</h3>

```diff
--- a/README.md
+++ b/README.md
@@ -85,7 +85,6 @@
 - [NANOG](https://www.nanog.org) - North American Network Operators' Group with fair share of automation presentations/discussions.
 - [Network to Coders Meetup](https://www.meetup.com/Network-to-Coders/) - Maybe this can pressure NTC to finally setup an event for the 140+ NTC meetup members.
 - [Puppetize Live](https://puppet.com/puppetizelive) - A 24-hour global event including community discussions, presentations, and training. Formerly PuppetConf.
-- [SaltStack NYC Meetup](https://www.meetup.com/SaltStack-NYC/) - Local NYC SaltStack user meetup.
 - [Tech Field Day](https://techfieldday.com/) - Field Day events bring together innovative IT product vendors and independent thought leaders to share information and opinions in a presentation and discussion format.
 - [SaltConf](https://saltconf.com/) - 4 days event including two days of SaltStack customer case studies and SaltStack technical deep dives.
 
```

<details>
<summary>Evidence and limitations</summary>

<p>Meetup.com, the platform that hosts the listed group, reports that the group does not exist. The listed URL redirects to the lowercase /saltstack-nyc/ path, which shows &#x27;Group not found – Sorry, the group you&#x27;re looking for doesn&#x27;t exist.&#x27; A Wayback snapshot from February 2025 shows the same message, so this has lasted more than a year and is not a temporary failure. The entry claims a local user meetup, and the resource no longer exists.</p>

<p>https://www.meetup.com/saltstack-nyc/ — Fetched 2026-11-10 with HTTP 200. The page reads &#x27;Group not found. Sorry, the group you&#x27;re looking for doesn&#x27;t exist.&#x27;</p>

<p>https://web.archive.org/web/20250215043040/https://www.meetup.com/saltstack-nyc/ — The February 2025 archived snapshot already shows the same &#x27;Group not found&#x27; page.</p>

<p>Caveats: I did not search for a renamed or successor Salt meetup group in NYC, and none was mentioned by the official Salt Project.</p>

</details>

<h3>DevNet Academy — update</h3>

```diff
--- a/README.md
+++ b/README.md
@@ -92,7 +92,7 @@
 # Training
 
 - [CML - Training videos @ learningnetwork.cisco.com](https://learningnetwork.cisco.com/s/cml-training-videos) - Learning and Certifications at Cisco has created a series of in-depth training videos to assist users with installing and operating Cisco Modeling Labs (CML). This video series also provides a few videos on some of the more advanced features that CML offers.
-- [DevNet Academy](https://devnet-academy.com) - Self-paced e-learning with theory, exercises and quizzes for the Cisco Certified DevNet Expert exam by Luca Gubler.
+- [DevNet Academy](https://devnet-academy.com) - Self-paced e-learning with theory, exercises and quizzes for the Cisco CCIE Automation (formerly DevNet Expert) exam by Luca Gubler.
 - [DevNet Expert Training](https://www.devnetexperttraining.com) - Training resources targeting the Cisco Certified DevNet Expert exam topics, including bootcamp courses by Andreas Baekdahl.
 - [GNS3 Academy - Instructor David Bombal](https://academy.gns3.com/courses/author/12794) - Offers an inexpensive set of introductions to Ansible and Python for Network Engineers, among other courses.
 - [ipSpace.net](https://www.ipspace.net/Training) - Numerous courses, webinars, and videos covering SDN, network automation, cloud computing, virtualization technologies, IPv6, VPNs, and much more.
```

<details>
<summary>Evidence and limitations</summary>

<p>The site is live and still offers Luca Gubler&#x27;s self-paced training with theory, exercises and quizzes. However, Cisco renamed the Cisco Certified DevNet Expert certification to CCIE Automation, effective February 3, 2026, and the site now markets itself as CCIE Automation training. The certification name in the description is out of date.</p>

<p>https://devnet-academy.com/ — The title is &#x27;CCIE Automation | Self-Paced Certification Training&#x27;. The page lists theory, videos, exercises, quizzes, mock labs, a workbook and optional 1:1 mentoring with Luca Gubler (DevNet Expert #20230004).</p>

<p>https://devnet-academy.com/blog/devnet-expert-becomes-ccie-automation-what-you-need-to-know/ — The site&#x27;s own post says &#x27;Cisco renamed DevNet Expert to CCIE Automation on February 3, 2026.&#x27;</p>

<p>https://ccie-automation.com/ — An unrelated trainer&#x27;s site independently states &#x27;DevNet Expert #20220006 (Rebranded to CCIE Automation)&#x27;.</p>

<p>Caveats: Cisco&#x27;s own Learning Network announcement page renders only with JavaScript, so the rename date comes from the training providers&#x27; statements and search summaries of Cisco&#x27;s announcement.</p>

</details>

<h3>GNS3 Academy - Instructor David Bombal — remove</h3>

```diff
--- a/README.md
+++ b/README.md
@@ -94,7 +94,6 @@
 - [CML - Training videos @ learningnetwork.cisco.com](https://learningnetwork.cisco.com/s/cml-training-videos) - Learning and Certifications at Cisco has created a series of in-depth training videos to assist users with installing and operating Cisco Modeling Labs (CML). This video series also provides a few videos on some of the more advanced features that CML offers.
 - [DevNet Academy](https://devnet-academy.com) - Self-paced e-learning with theory, exercises and quizzes for the Cisco Certified DevNet Expert exam by Luca Gubler.
 - [DevNet Expert Training](https://www.devnetexperttraining.com) - Training resources targeting the Cisco Certified DevNet Expert exam topics, including bootcamp courses by Andreas Baekdahl.
-- [GNS3 Academy - Instructor David Bombal](https://academy.gns3.com/courses/author/12794) - Offers an inexpensive set of introductions to Ansible and Python for Network Engineers, among other courses.
 - [ipSpace.net](https://www.ipspace.net/Training) - Numerous courses, webinars, and videos covering SDN, network automation, cloud computing, virtualization technologies, IPv6, VPNs, and much more.
 - [Model-Driven Network Configuration Tutorial](https://martimy.github.io/model-driven-configuration-tutorial) - Hands-on lab using Containerlab, NETCONF, gNMI, and YANG to configure Nokia SR Linux and Arista cEOS devices, focused on understanding the model layer before automation tooling.
 - [Network to Code](https://www.networktocode.com/training/) - Network Automation Training including Python, Ansible, DevOps, and much more.
```

<details>
<summary>Evidence and limitations</summary>

<p>The official GNS3 Academy no longer appears to offer the listed courses. The URL redirects to gns3.teachable.com, and the David Bombal author page lists no courses; its only category filters are CCNP, CCNA and Cisco, with no Ansible or Python. The former &#x27;Ansible for Network Engineers&#x27; course URL now redirects to the Academy homepage, and the /courses catalog says &#x27;Sorry, this school has no available products.&#x27; The entry&#x27;s specific claim (introductions to Ansible and Python by this instructor) is not supported by the current site.</p>

<p>https://gns3.teachable.com/courses/author/12794 — The author filter for David Bombal shows no course listings. The categories shown are only CCNP (1), CCNA (2) and Cisco (1). The footer reads © 2022 SolarWinds.</p>

<p>https://academy.gns3.com/p/ansible-for-network-engineers-gns3-ansible-cisco-network-automation — This former Bombal Ansible course URL (captured with HTTP 200 in 2017) now redirects to the gns3.teachable.com homepage.</p>

<p>https://gns3.teachable.com/courses — The catalog page reads &#x27;Sorry, this school has no available products ... No products found&#x27;.</p>

<p>Caveats: The homepage still shows promotional banners that may be stale. I did not log in to check for unlisted products.; David Bombal&#x27;s courses may be available elsewhere, but no officially documented successor for this listing was verified.</p>

</details>

<h3>Network to Code — update</h3>

```diff
--- a/README.md
+++ b/README.md
@@ -97,7 +97,7 @@
 - [GNS3 Academy - Instructor David Bombal](https://academy.gns3.com/courses/author/12794) - Offers an inexpensive set of introductions to Ansible and Python for Network Engineers, among other courses.
 - [ipSpace.net](https://www.ipspace.net/Training) - Numerous courses, webinars, and videos covering SDN, network automation, cloud computing, virtualization technologies, IPv6, VPNs, and much more.
 - [Model-Driven Network Configuration Tutorial](https://martimy.github.io/model-driven-configuration-tutorial) - Hands-on lab using Containerlab, NETCONF, gNMI, and YANG to configure Nokia SR Linux and Arista cEOS devices, focused on understanding the model layer before automation tooling.
-- [Network to Code](https://www.networktocode.com/training/) - Network Automation Training including Python, Ansible, DevOps, and much more.
+- [Network to Code](https://networktocode.com/how-we-do-it/training-enablement/) - Network Automation Training including Python, Ansible, DevOps, and much more.
 - [Network Programmability Basics - Cisco](https://developer.cisco.com/video/net-prog-basics/) - Jumpstart your journey into network programmability with this expert-led video course by Cisco DevNet.
 - [Nick Russo study resources](http://njrusmc.net/jobaid/jobaid.html) - Collection of DevNet certification study resources, such as study plans and Postman collections.
 - [Packet Coders](https://www.packetcoders.io/) - Gain Practical Real-World Knowledge with Packet Coders' On-Demand Training, Labs, and Private Code Repositories.
```

<details>
<summary>Evidence and limitations</summary>

<p>The listed URL permanently redirects (301) to https://networktocode.com/how-we-do-it/training-enablement/. That page still offers network automation training and says it develops &#x27;practical knowledge of Python, Ansible, APIs, structured data&#x27; alongside NetDevOps, DevOps for Networking and Nautobot training. The description is accurate, so only the URL needs updating to the canonical location.</p>

<p>https://networktocode.com/how-we-do-it/training-enablement/ — The original URL redirects here. The page title is &#x27;Training &amp; Enablement - Network to Code&#x27;. The text reads &#x27;Network Automation Training for Modern Network Teams ... Develop practical knowledge of Python, Ansible, APIs, structured data, and core network automation concepts&#x27;. It also mentions NTC University, the Enterprise Network Automation Academy and a Public Training Schedule.</p>

<p>Caveats: Plain curl requests to www.networktocode.com got a 403. A browser user agent got the 301 and the content.</p>

</details>

<h3>Nick Russo study resources — update</h3>

```diff
--- a/README.md
+++ b/README.md
@@ -99,7 +99,7 @@
 - [Model-Driven Network Configuration Tutorial](https://martimy.github.io/model-driven-configuration-tutorial) - Hands-on lab using Containerlab, NETCONF, gNMI, and YANG to configure Nokia SR Linux and Arista cEOS devices, focused on understanding the model layer before automation tooling.
 - [Network to Code](https://www.networktocode.com/training/) - Network Automation Training including Python, Ansible, DevOps, and much more.
 - [Network Programmability Basics - Cisco](https://developer.cisco.com/video/net-prog-basics/) - Jumpstart your journey into network programmability with this expert-led video course by Cisco DevNet.
-- [Nick Russo study resources](http://njrusmc.net/jobaid/jobaid.html) - Collection of DevNet certification study resources, such as study plans and Postman collections.
+- [Nick Russo study resources](https://web.archive.org/web/20240719051541/https://njrusmc.net/jobaid/jobaid.html) - Archived collection of Nick Russo's DevNet certification study resources, such as study plans and Postman collections.
 - [Packet Coders](https://www.packetcoders.io/) - Gain Practical Real-World Knowledge with Packet Coders' On-Demand Training, Labs, and Private Code Repositories.
 - [Python for Network Engineers](https://pynet.twb-tech.com/class.html) - Learn skills that make you better at network automation and that improve your capability to use programming to scale your work.
 
```

<details>
<summary>Evidence and limitations</summary>

<p>njrusmc.net is now a parked domain listed for sale: &#x27;Njrusmc.net is listed exclusively for sale on SerpDomains for $749.00&#x27;. The live link no longer serves Nick Russo&#x27;s resources. Nick Russo died in June 2024, and his site went offline afterwards. A July 2024 Wayback snapshot of the exact page preserves the content the entry describes: DevNet (DEVASC, DEVCOR, ENAUTO, SAUTO, SPAUTO) study plans and Postman collections. Pointing to the archive keeps this historic resource without sending readers to a domain sale page.</p>

<p>https://njrusmc.net/jobaid/jobaid.html — Fetched 2026-11-10. The page is a domain-sale listing: &#x27;Premium aged domain ... listed exclusively for sale on SerpDomains for $749.00&#x27;.</p>

<p>https://web.archive.org/web/20240719051541/https://njrusmc.net/jobaid/jobaid.html — The archived page &#x27;njrusmc.net/jobaid Job Aids&#x27; contains Certification Study Plans (DevNet Associate DEVASC, DEVCOR, ENAUTO, SAUTO, SPAUTO and others) and a &#x27;Postman Collections&#x27; section (RESTCONF, Meraki, DNA Center, SD-WAN, NSO and others).</p>

<p>https://github.com/kaelemc/NickRussoContent — A community (unofficial) archive of njrusmc.net content found via search. I did not use it as the replacement.</p>

<p>Caveats: Archive links depend on Internet Archive availability, which was intermittently offline during this research.; Nick Russo&#x27;s own GitHub repo (nickrusso42518/postman) appears to exist, but the GitHub API returned no metadata. It covers only the Postman part, so it is not proposed.</p>

</details>

<h3>IPEngineer - David Gee — update</h3>

```diff
--- a/README.md
+++ b/README.md
@@ -141,7 +141,7 @@
 - [Coding Packets](https://codingpackets.com/blog/) - The Network Automation thoughts of Brad Searle.
 - [dravetech.com](https://www.dravetech.com) - The Network Automation thoughts of David Barroso.
 - [Eric Chou - PythonicNetneg](https://blog.pythonicneteng.com/) - The Network Automation thoughts of Eric Chou.
-- [IPEngineer - David Gee](http://ipengineer.net) - Network automation, software-networking and musings from David Gee.
+- [IPEngineer - David Gee](https://dave.dev/) - Network automation, software-networking and musings from David Gee.
 - [ipSpace.net - Ivan Pepelnjak](https://blog.ipspace.net/tag/automation.html) - Network automation blog posts by Ivan Pepelnjak.
 - [Jason Edelman](http://www.jedelman.com/) - The Network Automation thoughts of Jason Edelman.
 - [Josh-V](https://josh-v.com/) - The Network Automation thoughts of Josh VanDeraa.
```

<details>
<summary>Evidence and limitations</summary>

<p>http://ipengineer.net now redirects to https://dave.dev/. That site describes itself as &#x27;Latest posts &amp; podcasts from built.fm, dave.dev &amp; historic content from ipengineer.net&#x27;, with posts by David Gee. The owner and content continue at the new canonical URL.</p>

<p>https://dave.dev/ — ipengineer.net redirects here. The page header reads &#x27;Latest posts &amp; podcasts from built.fm, dave.dev &amp; historic content from ipengineer.net &amp; arsonistgopher.com&#x27;. Posts by David Gee date through September 2025.</p>

<p>Caveats: Recent posts are broader (business, design, NATS) than network automation. The network automation material is mostly historic ipengineer content, which the description&#x27;s &#x27;and musings&#x27; already covers.; The entry name still says &#x27;IPEngineer&#x27;. A rename to &#x27;dave.dev&#x27; is optional and not proposed.</p>

</details>

<h3>ipSpace.net - Ivan Pepelnjak — update</h3>

```diff
--- a/README.md
+++ b/README.md
@@ -142,7 +142,7 @@
 - [dravetech.com](https://www.dravetech.com) - The Network Automation thoughts of David Barroso.
 - [Eric Chou - PythonicNetneg](https://blog.pythonicneteng.com/) - The Network Automation thoughts of Eric Chou.
 - [IPEngineer - David Gee](http://ipengineer.net) - Network automation, software-networking and musings from David Gee.
-- [ipSpace.net - Ivan Pepelnjak](https://blog.ipspace.net/tag/automation.html) - Network automation blog posts by Ivan Pepelnjak.
+- [ipSpace.net - Ivan Pepelnjak](https://blog.ipspace.net/tag/automation/) - Network automation blog posts by Ivan Pepelnjak.
 - [Jason Edelman](http://www.jedelman.com/) - The Network Automation thoughts of Jason Edelman.
 - [Josh-V](https://josh-v.com/) - The Network Automation thoughts of Josh VanDeraa.
 - [Mircea Ulinic](https://mirceaulinic.net/) - Random thoughts of Mircea Ulinic. May include event-driven network automation, vendor bashing or machine learning (TBD).
```

<details>
<summary>Evidence and limitations</summary>

<p>The blog moved from .html tag pages to directory-style URLs. https://blog.ipspace.net/tag/automation.html now resolves to https://blog.ipspace.net/tag/automation/. The tag index lists &#x27;automation (378)&#x27; posts, and the page shows recent posts from November 2026. The description is accurate, so only the URL needs canonicalizing.</p>

<p>https://blog.ipspace.net/tag/automation/ — The legacy .html URL resolves to this page. The tag index shows &#x27;automation (378)&#x27;, and the listed posts include November 2026 entries such as &#x27;candidate-active-configuration-iosxr&#x27;.</p>

<p>https://blog.ipspace.net/series/ — The series page links to &#x27;/tag/automation/&#x27; and also to automation-related series such as &#x27;Single Source of Truth (SSoT) in Network Automation&#x27;.</p>

</details>

<h3>DevNet Expert Training — update</h3>

```diff
--- a/README.md
+++ b/README.md
@@ -93,7 +93,7 @@
 
 - [CML - Training videos @ learningnetwork.cisco.com](https://learningnetwork.cisco.com/s/cml-training-videos) - Learning and Certifications at Cisco has created a series of in-depth training videos to assist users with installing and operating Cisco Modeling Labs (CML). This video series also provides a few videos on some of the more advanced features that CML offers.
 - [DevNet Academy](https://devnet-academy.com) - Self-paced e-learning with theory, exercises and quizzes for the Cisco Certified DevNet Expert exam by Luca Gubler.
-- [DevNet Expert Training](https://www.devnetexperttraining.com) - Training resources targeting the Cisco Certified DevNet Expert exam topics, including bootcamp courses by Andreas Baekdahl.
+- [CCIE Automation Training](https://ccie-automation.com/) - Training resources targeting the Cisco CCIE Automation (formerly DevNet Expert) exam topics, including bootcamp courses by Andreas Baekdahl.
 - [GNS3 Academy - Instructor David Bombal](https://academy.gns3.com/courses/author/12794) - Offers an inexpensive set of introductions to Ansible and Python for Network Engineers, among other courses.
 - [ipSpace.net](https://www.ipspace.net/Training) - Numerous courses, webinars, and videos covering SDN, network automation, cloud computing, virtualization technologies, IPv6, VPNs, and much more.
 - [Model-Driven Network Configuration Tutorial](https://martimy.github.io/model-driven-configuration-tutorial) - Hands-on lab using Containerlab, NETCONF, gNMI, and YANG to configure Nokia SR Linux and Arista cEOS devices, focused on understanding the model layer before automation tooling.
```

<details>
<summary>Evidence and limitations</summary>

<p>www.devnetexperttraining.com and devnetexperttraining.com both return HTTP 301 to https://ccie-automation.com/, titled &#x27;Get Cisco Certified in Automation - ccie-automation.com by Andreas Baekdahl&#x27;. This is the same instructor, now offering CCIE Automation (formerly DevNet Expert, renamed by Cisco on February 3, 2026) masterclasses plus CCNP Automation courses. The destination and description should reflect the canonical site and the renamed exam.</p>

<p>https://ccie-automation.com/ — The page is &#x27;ccie-automation.com by Andreas Baekdahl&#x27;. It offers a live 9-day CCIE Automation Masterclass covering v1.1 and v1.2, an on-demand CCIE course and a CCNP Automation course. The instructor is listed as &#x27;CCIE×4, CCDE, first DevNet Expert&#x27;, and it states &#x27;DevNet Expert ... (Rebranded to CCIE Automation)&#x27;.</p>

<p>https://devnet-academy.com/blog/devnet-expert-becomes-ccie-automation-what-you-need-to-know/ — States &#x27;Cisco renamed DevNet Expert to CCIE Automation on February 3, 2026.&#x27;</p>

<p>Caveats: The old domain&#x27;s TLS certificate does not match its hostname. I saw the 301 only by ignoring certificate validation (curl -k), so browsers will show a certificate error on the old URL.</p>

<p>Source snapshot incomplete; excluded from the saved baseline.</p>

</details>

<h3>Network to Code — update</h3>

```diff
--- a/README.md
+++ b/README.md
@@ -148,7 +148,7 @@
 - [Mircea Ulinic](https://mirceaulinic.net/) - Random thoughts of Mircea Ulinic. May include event-driven network automation, vendor bashing or machine learning (TBD).
 - [MTU Ninja](https://vincent.bernat.ch/en/blog#tag-network-automation) - The Network Automation thoughts of Vincent Bernat.
 - [Napalm-automation](https://napalm-automation.net/blog/) - News and updates about the NAPALM project.
-- [Network to Code](https://blog.networktocode.com/) - Network to Code's blog sharing thoughts, ideas, and tips all about network automation.
+- [Network to Code](https://networktocode.com/blog/) - Network to Code's blog sharing thoughts, ideas, and tips all about network automation.
 - [Networklore](https://networklore.com/blog) - The Network Automation thoughts of Patrick Ogenstad.
 - [Network OP](https://networkop.co.uk/) - The Network Automation thoughts of Michael Kashin.
 - [NWMichl Blog](https://nwmichl.net/) - The Network Automation thoughts of Michael Schön.
```

<details>
<summary>Evidence and limitations</summary>

<p>https://blog.networktocode.com/ now 301-redirects to the networktocode.com homepage, not to a blog. The blog itself is at https://networktocode.com/blog/, which describes itself as covering network automation and has posts up to Nov 2026. The description is still accurate; only the URL needs to change.</p>

<p>https://blog.networktocode.com/ — Returns HTTP 301 with a Location header pointing to http://networktocode.com/ (the homepage, not a blog page).</p>

<p>https://networktocode.com/blog/ — This is the Network to Code blog: &#x27;Insights and inspiration from the experts helping organizations simplify, scale, and accelerate network automation.&#x27; Recent posts include &#x27;Last Month in Nautobot – October 2026&#x27; (Nov 10, 2026).</p>

<p>Caveats: Direct curl requests got a Cloudflare/WP Engine 403 bot block. The content was read through an alternate fetcher.</p>

</details>

<h3>NWMichl Blog — update</h3>

```diff
--- a/README.md
+++ b/README.md
@@ -151,7 +151,7 @@
 - [Network to Code](https://blog.networktocode.com/) - Network to Code's blog sharing thoughts, ideas, and tips all about network automation.
 - [Networklore](https://networklore.com/blog) - The Network Automation thoughts of Patrick Ogenstad.
 - [Network OP](https://networkop.co.uk/) - The Network Automation thoughts of Michael Kashin.
-- [NWMichl Blog](https://nwmichl.net/) - The Network Automation thoughts of Michael Schön.
+- [NWMichl Blog](https://nwmichl.wordpress.com/) - The Network Automation thoughts of Michael Schön.
 - [Open-Source Routing and Network Simulation - Brian Linkletter](https://www.brianlinkletter.com/) - Blog about the open-source network emulation and network simulation tools by Brian Linkletter.
 - [OpsMill Blog](https://opsmill.com/blog/) - Business strategy & technical deep dives for powering infrastructure automation.
 - [Packet Coders](https://packetcoders.io/tag/blog) - The Network Automation thoughts of Rick Donato.
```

<details>
<summary>Evidence and limitations</summary>

<p>nwmichl.net now serves an unrelated Indonesian online-lottery spam page; the Wayback Machine already shows this in Aug 2026. The author&#x27;s blog is still live at nwmichl.wordpress.com under the same name, &#x27;NWMichl Blog&#x27;. Its About page names Michael Schön and refers to the nwmichl.net domain, which confirms it is the same author and blog. The description is still accurate.</p>

<p>https://nwmichl.net/ — Returns HTTP 200 with the title &#x27;SENGTOTO 💰 Trik Rahasia Menang Togel Online dengan Pola Angka Jitu&#x27;, a gambling/spam page with no network automation content.</p>

<p>http://web.archive.org/web/20260811224411/https://nwmichl.net/ — The Wayback snapshot from 2026-08-11 already shows the same gambling spam page.</p>

<p>https://nwmichl.wordpress.com/ — Returns HTTP 200 with the title &#x27;NWMichl Blog – Networking, Automation, Infrastructure as code, Telemetry&#x27;. Posts include &#x27;Chatops with Python &amp; FastAPI&#x27; (June 28, 2021) and &#x27;Working With Static Inventories&#x27;.</p>

<p>https://nwmichl.wordpress.com/about/ — The About page names the author as Michael Schön and refers to the nwmichl.net domain (RSS/contact).</p>

<p>Caveats: The newest post I saw is from 2021. The blog is historic but still relevant.; The current link points readers to a spam site, so this change is time-sensitive.</p>

</details>

<h3>Napalm-automation — remove</h3>

```diff
--- a/README.md
+++ b/README.md
@@ -147,7 +147,6 @@
 - [Josh-V](https://josh-v.com/) - The Network Automation thoughts of Josh VanDeraa.
 - [Mircea Ulinic](https://mirceaulinic.net/) - Random thoughts of Mircea Ulinic. May include event-driven network automation, vendor bashing or machine learning (TBD).
 - [MTU Ninja](https://vincent.bernat.ch/en/blog#tag-network-automation) - The Network Automation thoughts of Vincent Bernat.
-- [Napalm-automation](https://napalm-automation.net/blog/) - News and updates about the NAPALM project.
 - [Network to Code](https://blog.networktocode.com/) - Network to Code's blog sharing thoughts, ideas, and tips all about network automation.
 - [Networklore](https://networklore.com/blog) - The Network Automation thoughts of Patrick Ogenstad.
 - [Network OP](https://networkop.co.uk/) - The Network Automation thoughts of Michael Kashin.
```

<details>
<summary>Evidence and limitations</summary>

<p>The listed blog page returns 404 and the napalm-automation.net homepage is now an unrelated &#x27;Napalm Automation - All about API&#x27; content site. Official NAPALM metadata no longer points there. The napalm-automation GitHub org&#x27;s website field is napalm.readthedocs.io. The repository that built napalm-automation.net (napalm-automation.github.io) is archived, with its last push in July 2021. I found no official NAPALM blog successor; the official docs are not a blog equivalent.</p>

<p>https://napalm-automation.net/blog/ — Returns HTTP 404 &#x27;page not found&#x27;.</p>

<p>https://napalm-automation.net/ — Returns HTTP 200 with the title &#x27;Napalm Automation - All about API&#x27;. It shows generic articles about Google APIs (e.g. Android Sleep API) by &#x27;Gay Homenick&#x27;, with nothing about the NAPALM project.</p>

<p>https://api.github.com/orgs/napalm-automation — The org &#x27;blog&#x27; field is https://napalm.readthedocs.io/en/latest/, not napalm-automation.net.</p>

<p>https://api.github.com/repos/napalm-automation/napalm-automation.github.io — The repository has homepage https://napalm-automation.net, archived: true, and pushed_at 2021-07-15. This is the official site source, now archived.</p>

<p>https://github.com/napalm-automation/napalm — The README points to napalm.readthedocs.io and Slack, and does not mention napalm-automation.net.</p>

<p>Caveats: The old blog content may still exist in the archived napalm-automation.github.io repository. A maintainer could instead link to that historic archive, but I did not verify what it contains.</p>

<p>Source snapshot incomplete; excluded from the saved baseline.</p>

</details>

<h3>Getting Started and Basics — replace</h3>

<p>0 proposed change(s); 1 held for unresolved questions.</p>

<details>
<summary>Evidence and limitations</summary>

<p>yaml.org/start.html now returns 404 on the official YAML site (http://www.yaml.org redirects to https://yaml.org). The yaml.org homepage now sends learners to yaml.info (&#x27;Learn about YAML!&#x27;), which offers &#x27;A YAML Tutorial and Reference&#x27; and is maintained by Tina Müller (a YAML maintainer). That makes yaml.info the most plausible official introduction.</p>

<p>https://yaml.org/start.html — http://www.yaml.org/start.html redirects to https://yaml.org/start.html, which returns HTTP 404 (&#x27;404 - Not found&#x27; in the yaml/www.yaml.org MkDocs site).</p>

<p>https://yaml.org/ — The official homepage lists the spec versions and links &#x27;YAML Information: https://yaml.info/ – Learn about YAML!&#x27;. It has no getting-started page of its own.</p>

<p>https://yaml.info/ — The site gives information on the YAML serialization language and has a &#x27;Learn YAML&#x27; section (&#x27;A YAML Tutorial and Reference&#x27;). It is maintained by Tina Müller, with source at github.com/perlpunk/yaml.info, and notes it is still under development.</p>

<p>Blocking questions: yaml.org does not explicitly state that yaml.info replaces start.html. It is only linked from the homepage as the learning resource, so a maintainer should confirm the substitution.; The entry name &#x27;Getting Started and Basics&#x27; may need adjusting to match yaml.info (e.g. &#x27;YAML Information&#x27;). I did not propose a new name.</p>

<p>Caveats: yaml.info says it is under development and that links may change.; I could not read the archived start.html (Wayback returned 429), so I could not compare its original content.</p>

<p>Source snapshot incomplete; excluded from the saved baseline.</p>

</details>

<h3>YAML syntax validator — update</h3>

```diff
--- a/README.md
+++ b/README.md
@@ -170,7 +170,7 @@
  - [Online Validator](https://yaml-online-parser.appspot.com/) - Online YAML Parser.
  - [Sample YAML documents describing common data structures](https://github.com/ipspace/NetOpsWorkshop/tree/master/YAML) - YAML examples courtesy of Ivan Pepelnjak.
  - [YAML Data Validation with JSON Schema](https://infrastructureascode.ch/yaml_validation.html) - Explains how JSON schema can be used to validate YAML files and how syntax highlighting can be added to the IDE for the YAML files.
- - [YAML syntax validator](https://yamllint.readthedocs.io/en/latest/) - YAML online parser.
+ - [YAML syntax validator](https://yamllint.readthedocs.io/en/latest/) - A linter for YAML files that checks syntax validity as well as key repetition and cosmetic problems.
  - [YAML idiosyncrasies](https://docs.saltstack.com/en/latest/topics/troubleshooting/yaml_idiosyncrasies.html) -- Document with the most common YAML idiosyncrasies, hosted under the SaltStack docs, but not specific to Salt or any other tool.
 
 ### JSON
```

<details>
<summary>Evidence and limitations</summary>

<p>The URL is the official yamllint documentation and still fits the YAML section. The description is wrong: yamllint is a linter for YAML files that you install and run, not an online parser. The docs say it checks syntax validity and also problems such as duplicate keys and cosmetic issues.</p>

<p>https://yamllint.readthedocs.io/en/latest/ — The page loads and is titled &#x27;yamllint 1.38.0 documentation&#x27;. It reads: &#x27;A linter for YAML files. yamllint does not only check for syntax validity, but for weirdnesses like key repetition and cosmetic problems such as lines length, trailing spaces, indentation, etc.&#x27; Its contents cover Installing yamllint, Running yamllint, Configuration, Rules and editor integration. There is no online parser.</p>

<p>Caveats: The entry name &#x27;YAML syntax validator&#x27; is generic but not false, so no rename is proposed. A maintainer may prefer &#x27;yamllint&#x27;.; I did not install or run yamllint.</p>

</details>

<h3>JSON 2 YAML — update</h3>

```diff
--- a/README.md
+++ b/README.md
@@ -178,7 +178,7 @@
  - [Awesome JSON](https://github.com/burningtree/awesome-json) - A curated list of awesome JSON libraries and resources.
  - [Getting Started and Basics](https://www.codecademy.com/courses/javascript-beginner-en-xTAfX/0/1) - JSON Basics.
  - [JSON diff](https://extendsclass.com/json-diff.html) - An online JSON diff tool.
- - [JSON 2 YAML](https://www.json2yaml.com/) - An online JSON to YAML conversion tool.
+ - [JSON 2 YAML](https://www.bairesdev.com/tools/json2yaml/) - An online JSON to YAML conversion tool.
  - [JSON Viewer Tool](https://jsonviewertool.com/json-to-yaml) - Free client-side JSON to YAML converter with configurable output (indent, quoting, null style).
 
 ### XML
```

<details>
<summary>Evidence and limitations</summary>

<p>json2yaml.com now permanently redirects (HTTP 301) to a JSON-to-YAML converter on bairesdev.com. The redirect is issued by the json2yaml.com domain itself, and the target still matches the description. The suggested change is the URL only, to the redirect target, which is also the page&#x27;s canonical URL.</p>

<p>https://www.json2yaml.com/ — A HEAD request returns HTTP/2 301 with &#x27;location: https://www.bairesdev.com/tools/json2yaml/&#x27;.</p>

<p>https://www.bairesdev.com/tools/json2yaml/ — The page title is &#x27;JSON to YAML Online Converter&#x27;. Its canonical link and og:url are bairesdev.com/tools/json2yaml, and its meta description mentions a &#x27;json2yaml online editor&#x27;. The rendered text shows JSON and YAML panes.</p>

<p>Caveats: The page is mostly rendered by JavaScript, and I did not run a conversion.; The tool is now hosted by BairesDev, a vendor. The original json2yaml.com URL still works through the redirect.</p>

</details>

<h3>Cisco Labs YANG Introduction — update</h3>

```diff
--- a/README.md
+++ b/README.md
@@ -187,7 +187,7 @@
 
 ### YANG
 
- - [Cisco Labs YANG Introduction](https://developer.cisco.com/learning/lab/intro-yang/step/1) - Introducing YANG Data Modeling for the Network.
+ - [Cisco Labs YANG Introduction](https://developer.cisco.com/learning/labs/intro-yang/) - Introducing YANG Data Modeling for the Network.
  - [IETF RFC](https://tools.ietf.org/html/rfc6020) - The IETF RFC on YANG.
  - [YANG for dummies](https://napalm-automation.net/yang-for-dummies/) - NAPALM YANG introduction.
  - [YANG fundamentals](https://www.devnetexperttraining.com/devnet-articles/yang-fundamentals) - A walkthrough video on how to build your own YANG model.
```

<details>
<summary>Evidence and limitations</summary>

<p>The Cisco DevNet lab still exists. Its title, &#x27;Introducing YANG Data Modeling for the Network&#x27;, matches the description. However, the listed step URL is a JavaScript-app route whose canonical link points to the generic Learning Labs Center. The lab&#x27;s own canonical URL is /learning/labs/intro-yang/.</p>

<p>https://developer.cisco.com/learning/labs/intro-yang/ — The page has rel=canonical and og:url set to https://developer.cisco.com/learning/labs/intro-yang/. Its meta description reads: &#x27;What&#x27;s YANG got to do with it? ... Learn about the YANG modeling language, checkout some of the available model options, and even see what network data looks like when fit into those models!&#x27;</p>

<p>https://developer.cisco.com/learning/labs/intro-yang/introduction/ — The page title is &#x27;Introduction - Introducing YANG Data Modeling for the Network - Cisco DevNet Learning Labs Center&#x27;.</p>

<p>https://developer.cisco.com/learning/lab/intro-yang/step/1/ — The listed URL returns 200, but its metadata is generic: the title is &#x27;Learning Labs Center - Cisco DevNet&#x27; and the canonical is https://developer.cisco.com/learning/.</p>

<p>Caveats: The site is a JavaScript app, and I read only the server-rendered metadata, not the lab steps.</p>

</details>

<h3>IETF RFC — update</h3>

```diff
--- a/README.md
+++ b/README.md
@@ -188,7 +188,7 @@
 ### YANG
 
  - [Cisco Labs YANG Introduction](https://developer.cisco.com/learning/lab/intro-yang/step/1) - Introducing YANG Data Modeling for the Network.
- - [IETF RFC](https://tools.ietf.org/html/rfc6020) - The IETF RFC on YANG.
+ - [IETF RFC](https://www.rfc-editor.org/info/rfc6020/) - The IETF RFC on YANG.
  - [YANG for dummies](https://napalm-automation.net/yang-for-dummies/) - NAPALM YANG introduction.
  - [YANG fundamentals](https://www.devnetexperttraining.com/devnet-articles/yang-fundamentals) - A walkthrough video on how to build your own YANG model.
 
```

<details>
<summary>Evidence and limitations</summary>

<p>tools.ietf.org now redirects to the official RFC Editor page for RFC 6020. RFC 6020 (YANG 1.0) is still a standards-track RFC: it is updated by RFC 9890, not obsoleted. The description stays accurate, so the change is to the canonical URL only.</p>

<p>https://tools.ietf.org/html/rfc6020 — The URL redirects to https://www.rfc-editor.org/info/rfc6020/.</p>

<p>https://www.rfc-editor.org/info/rfc6020/ — The page title is &#x27;RFC 6020: YANG - A Data Modeling Language for the Network Configuration Protocol (NETCONF)&#x27;. It is a standards-track document from the NETMOD working group, published October 2010, and is &#x27;Updated by (1) RFC 9890&#x27;. I saw no &#x27;obsoleted by&#x27; entry.</p>

<p>Caveats: YANG 1.1 is defined separately in RFC 7950. A maintainer could optionally mention it, but the current entry is not false.; The current link still works through the redirect, so updating it is optional housekeeping.</p>

</details>

<h3>Documentation — update</h3>

```diff
--- a/README.md
+++ b/README.md
@@ -194,7 +194,7 @@
 
 ### Jinja2
 
- - [Documentation](http://jinja.pocoo.org/docs/2.10/templates/) - Base documentation for Jinja2.
+ - [Documentation](https://jinja.palletsprojects.com/en/stable/templates/) - Base documentation for Jinja2.
  - [Sample Jinja2 templates](https://github.com/ipspace/NetOpsWorkshop/tree/master/Jinja2) - Jinja examples courtesy of Ivan Pepelnjak.
 
 ## API
```

<details>
<summary>Evidence and limitations</summary>

<p>The old jinja.pocoo.org URL for version 2.10 now redirects to the official Pallets Jinja template docs for the stable version. The resource is still the core Jinja template documentation. The change is to the canonical URL; the description stays.</p>

<p>http://jinja.pocoo.org/docs/2.10/templates/ — The URL redirects to https://jinja.palletsprojects.com/en/stable/templates/ and returns HTTP 200.</p>

<p>https://jinja.palletsprojects.com/en/stable/templates/ — This is the official Pallets-hosted Jinja template designer documentation. The snapshot hash in the packet was taken from this redirect target.</p>

<p>Caveats: The project is now branded &#x27;Jinja&#x27; rather than &#x27;Jinja2&#x27;, but &#x27;Jinja2&#x27; in the description is not materially false. I did not read the whole page.</p>

</details>

<h3>YAML idiosyncrasies — update</h3>

```diff
--- a/README.md
+++ b/README.md
@@ -171,7 +171,7 @@
  - [Sample YAML documents describing common data structures](https://github.com/ipspace/NetOpsWorkshop/tree/master/YAML) - YAML examples courtesy of Ivan Pepelnjak.
  - [YAML Data Validation with JSON Schema](https://infrastructureascode.ch/yaml_validation.html) - Explains how JSON schema can be used to validate YAML files and how syntax highlighting can be added to the IDE for the YAML files.
  - [YAML syntax validator](https://yamllint.readthedocs.io/en/latest/) - YAML online parser.
- - [YAML idiosyncrasies](https://docs.saltstack.com/en/latest/topics/troubleshooting/yaml_idiosyncrasies.html) -- Document with the most common YAML idiosyncrasies, hosted under the SaltStack docs, but not specific to Salt or any other tool.
+ - [YAML idiosyncrasies](https://docs.saltproject.io/en/latest/topics/troubleshooting/yaml_idiosyncrasies.html) -- Document with the most common YAML idiosyncrasies, hosted under the SaltStack docs, but not specific to Salt or any other tool.
 
 ### JSON
 
```

<details>
<summary>Evidence and limitations</summary>

<p>The old docs.saltstack.com URL for this page returns 404, though the docs.saltstack.com root still loads. The same &#x27;YAML Idiosyncrasies&#x27; page is live on the current official Salt Project docs domain. The page is mostly about general YAML pitfalls (tabs vs spaces, indentation, and so on), so the description holds.</p>

<p>https://docs.saltstack.com/en/latest/topics/troubleshooting/yaml_idiosyncrasies.html — Returns HTTP/2 404 with no redirect.</p>

<p>https://docs.saltproject.io/en/latest/topics/troubleshooting/yaml_idiosyncrasies.html — Returns 200 on the Salt Project docs, under Using Salt &gt; Troubleshooting &gt; YAML Idiosyncrasies. It begins: &#x27;YAML is a general purpose system and there are a number of things that would seem to make sense in an sls file that cause YAML issues&#x27;, and covers &#x27;Spaces vs Tabs&#x27; among other topics.</p>

<p>Caveats: The page is written in the context of Salt SLS files, so &#x27;not specific to Salt&#x27; is the list&#x27;s own characterisation. Most of the content is general YAML pitfalls.; A versioned copy also exists at docs.saltproject.io/en/3006/.</p>

<p>Source snapshot incomplete; excluded from the saved baseline.</p>

</details>

<h3>YANG for dummies — update</h3>

```diff
--- a/README.md
+++ b/README.md
@@ -189,7 +189,7 @@
 
  - [Cisco Labs YANG Introduction](https://developer.cisco.com/learning/lab/intro-yang/step/1) - Introducing YANG Data Modeling for the Network.
  - [IETF RFC](https://tools.ietf.org/html/rfc6020) - The IETF RFC on YANG.
- - [YANG for dummies](https://napalm-automation.net/yang-for-dummies/) - NAPALM YANG introduction.
+ - [YANG for dummies](https://github.com/napalm-automation/napalm-automation.github.io/blob/master/_posts/2017/2017-08-14-yang-for-dummies.md) - NAPALM YANG introduction.
  - [YANG fundamentals](https://www.devnetexperttraining.com/devnet-articles/yang-fundamentals) - A walkthrough video on how to build your own YANG model.
 
 ### Jinja2
```

<details>
<summary>Evidence and limitations</summary>

<p>The NAPALM blog domain napalm-automation.net now serves unrelated content: 2026 posts about residential proxies and Google Maps scraper APIs. The original post returns 404. The post&#x27;s source (David Barroso, 14 Aug 2017, &#x27;YANG for dummies&#x27;) is still in the official, now-archived NAPALM website repository, whose CNAME is napalm-automation.net. The github.io mirror also redirects to the taken-over domain, so the GitHub source file is the stable official copy.</p>

<p>https://napalm-automation.net/yang-for-dummies/ — Returns 404.</p>

<p>https://napalm-automation.net/ — The homepage now lists unrelated posts such as &#x27;Best 10 Residential Proxies for Small Teams 2026&#x27; and &#x27;Top 6 Google Maps Scraper APIs Without Managing Proxies 2026&#x27;. There is no NAPALM content.</p>

<p>https://github.com/napalm-automation/napalm-automation.github.io/blob/master/_posts/2017/2017-08-14-yang-for-dummies.md — Returns 200. The post source is in napalm-automation/napalm-automation.github.io (&#x27;The NAPALM website&#x27;, isArchived true, last commit 2021-07-15). Its CNAME is napalm-automation.net and _config.yml sets url https://napalm-automation.net.</p>

<p>http://web.archive.org/web/20201206181611/https://napalm-automation.net/yang-for-dummies/ — The 2020 capture shows &#x27;YANG for dummies By David Barroso Posted August 14, 2017&#x27;, an introduction to YANG originally written for the napalm-yang docs. This matches the entry.</p>

<p>Caveats: The GitHub URL shows Jekyll markdown source rather than a rendered page. A maintainer may prefer the Wayback Machine capture instead.; The napalm-yang project the post refers to is itself archived. The post is historic introductory material on YANG.</p>

<p>Source snapshot incomplete; excluded from the saved baseline.</p>

</details>

<h3>YANG fundamentals — update</h3>

```diff
--- a/README.md
+++ b/README.md
@@ -190,7 +190,7 @@
  - [Cisco Labs YANG Introduction](https://developer.cisco.com/learning/lab/intro-yang/step/1) - Introducing YANG Data Modeling for the Network.
  - [IETF RFC](https://tools.ietf.org/html/rfc6020) - The IETF RFC on YANG.
  - [YANG for dummies](https://napalm-automation.net/yang-for-dummies/) - NAPALM YANG introduction.
- - [YANG fundamentals](https://www.devnetexperttraining.com/devnet-articles/yang-fundamentals) - A walkthrough video on how to build your own YANG model.
+ - [YANG fundamentals](https://www.youtube.com/watch?v=Qyn-BrQTXpc) - A walkthrough video on how to build your own YANG model.
 
 ### Jinja2
 
```

<details>
<summary>Evidence and limitations</summary>

<p>devnetexperttraining.com now redirects (301) to the ccie-automation.com homepage. The new site belongs to the same author, Andreas Baekdahl, and links its Trustpilot reviews under devnetexperttraining.com. The original &#x27;YANG fundamentals&#x27; article only embedded a YouTube video, and that video is still live on the author&#x27;s &#x27;CCIE Automation / Andreas Baekdahl&#x27; channel.</p>

<p>https://www.devnetexperttraining.com/devnet-articles/yang-fundamentals — The TLS certificate does not cover the hostname. Ignoring that, the domain returns 301 to https://ccie-automation.com/. ccie-automation.com/devnet-articles/yang-fundamentals returns 404, and the new site&#x27;s sitemap has no YANG page.</p>

<p>http://web.archive.org/web/20240920225244/https://www.devnetexperttraining.com/devnet-articles/yang-fundamentals — The September 2024 capture has the heading &#x27;YANG fundamentals&#x27; and an embedded &#x27;YouTube Video, YANG fundamentals&#x27; at youtube.com/embed/Qyn-BrQTXpc.</p>

<p>https://www.youtube.com/watch?v=Qyn-BrQTXpc — YouTube oEmbed returns the title &#x27;YANG fundamentals&#x27; and the author &#x27;CCIE Automation / Andreas Baekdahl&#x27; (@ccie-automation).</p>

<p>https://ccie-automation.com/ — The site is titled &#x27;ccie-automation.com by Andreas Baekdahl&#x27; and links to trustpilot.com/review/devnetexperttraining.com, which shows the same owner.</p>

<p>Caveats: I did not watch the video, so the claim that it shows how to build your own YANG model rests on the original article and the video title.</p>

<p>Source snapshot incomplete; excluded from the saved baseline.</p>

</details>

<h3>RESTCONF requests for IOS-XE — update</h3>

```diff
--- a/README.md
+++ b/README.md
@@ -201,7 +201,7 @@
 
 ### RESTCONF
 
- - [RESTCONF requests for IOS-XE](https://www.devnetexperttraining.com/articles/restconf-operations) - How to combine HTTP path, method and payload for IOS-XE restconf operations.
+ - [RESTCONF requests for IOS-XE](https://ccie-automation.com/blog/iosxe-list-operations/) - How to combine HTTP path, method and payload for IOS-XE restconf operations.
 
 ### NETCONF
 
```

<details>
<summary>Evidence and limitations</summary>

<p>devnetexperttraining.com redirects to the ccie-automation.com homepage; the author is the same, Andreas Baekdahl. The original article, &#x27;IOS-XE RESTCONF list element operations - Combining API endpoints, payloads and methods&#x27;, is republished on the new site&#x27;s blog under the same title. It covers the same GET/POST/PUT/PATCH method, path and payload combinations, so the description still fits.</p>

<p>https://www.devnetexperttraining.com/articles/restconf-operations — The TLS certificate does not match the hostname, and the domain 301-redirects to the https://ccie-automation.com/ root. The old path on the new domain returns 404.</p>

<p>http://web.archive.org/web/2023/https://www.devnetexperttraining.com/articles/restconf-operations — The archived page has the title &#x27;IOS-XE RESTCONF list element operations&#x27; and the subtitle &#x27;Combining API endpoints, payloads and methods&#x27;. It covers supported HTTP methods, endpoint paths and JSON payloads on IOS-XE.</p>

<p>https://ccie-automation.com/blog/iosxe-list-operations/ — The page is titled &#x27;IOS XE RESTCONF - List element operations&#x27;. It has sections on HTTP GET, POST (including the &#x27;POST on list must be on list element&#x27; error), PUT and PATCH for lists, list items and containers.</p>

<p>Caveats: There is no path-level redirect; the match is based on same author and matching content.</p>

<p>Source snapshot incomplete; excluded from the saved baseline.</p>

</details>

<h3>NETCONF message layers — update</h3>

```diff
--- a/README.md
+++ b/README.md
@@ -205,7 +205,7 @@
 
 ### NETCONF
 
- - [NETCONF message layers](https://www.devnetexperttraining.com/articles/netconf-anatomy) - A view into the payload of NETCONF XML documents and layers.
+ - [NETCONF message layers](https://ccie-automation.com/blog/netconf-anatomy/) - A view into the payload of NETCONF XML documents and layers.
 
 ## Python
 
```

<details>
<summary>Evidence and limitations</summary>

<p>The &#x27;NETCONF anatomy&#x27; article from devnetexperttraining.com is republished, with the same opening text, on the author&#x27;s current site, ccie-automation.com. The old domain only redirects to the new site&#x27;s homepage.</p>

<p>https://www.devnetexperttraining.com/articles/netconf-anatomy — The TLS certificate does not match the hostname, and the domain 301-redirects to https://ccie-automation.com/. The same path on the new domain returns 404.</p>

<p>http://web.archive.org/web/20231202053408/https://www.devnetexperttraining.com/articles/netconf-anatomy — The original article, &#x27;The anatomy of NETCONF&#x27;, begins: &#x27;In this article we will examine the basic characteristics of the NETCONF protocol as defined by the original RFC 6241.&#x27;</p>

<p>https://ccie-automation.com/blog/netconf-anatomy/ — The page is titled &#x27;NETCONF anatomy - A look under the hood&#x27;, by Andreas Baekdahl, and has the identical opening sentence referencing RFC 6241.</p>

<p>Caveats: There is no path-level redirect; the match is based on same author and identical content. I did not compare the full article.</p>

<p>Source snapshot incomplete; excluded from the saved baseline.</p>

</details>

<h3>Python data structures — update</h3>

```diff
--- a/README.md
+++ b/README.md
@@ -212,7 +212,7 @@
  - [Awesome Python](https://github.com/vinta/awesome-python) - A curated list of awesome Python frameworks, libraries, software and resources.
  - [Learn Python the Hard Way](https://learnpythonthehardway.org) - Learn Python The Hard Way takes you from absolute zero to able to read and write basic Python, giving you the tools to understand other documentation and books about Python.
  - [Python at Codecademy](https://www.codecademy.com/learn/learn-python-3) - Learn Python by Codecademy.
- - [Python data structures](https://www.devnetexperttraining.com/articles/python-looping) - Examples on how to access data in nested structures of lists and dicts.
+ - [Python data structures](https://ccie-automation.com/blog/python-lists-and-dicts/) - Examples on how to access data in nested structures of lists and dicts.
  - [Python Programming Guides and Tutorials - Python Central](https://pythoncentral.io/) - Experienced Python programmers and enthusiasts from around the world that are eager to share their experience.
  - [Real Python](https://www.realpython.com) - Real Python is a leading provider of online Python education. They regularly publish new articles, books, courses, and videos of basic to advanced Python concepts.
 
```

<details>
<summary>Evidence and limitations</summary>

<p>The &#x27;Python looping&#x27; article on nested lists and dicts is republished as &#x27;Nested Python lists and dicts - Looping and direct access&#x27; on the author&#x27;s current site, ccie-automation.com. The old domain only redirects to the new site&#x27;s homepage. The content matches the description.</p>

<p>https://www.devnetexperttraining.com/articles/python-looping — The TLS certificate does not match the hostname, and the domain redirects to the https://ccie-automation.com/ root. The same path on the new domain returns 404.</p>

<p>https://ccie-automation.com/blog/python-lists-and-dicts/ — The page is titled &#x27;Nested Python lists and dicts - Looping and direct access&#x27;. Sections include looping through and directly accessing lists, dicts, lists of lists, lists of dicts, dicts of lists and dicts of dicts.</p>

<p>https://ccie-automation.com/ — The site is by Andreas Baekdahl and links to trustpilot.com/review/devnetexperttraining.com, confirming the old and new domains have the same owner.</p>

<p>Caveats: There is no path-level redirect. I could not load the Wayback copy of the original python-looping page (archive rate limiting), so the identification rests on the matching topic and the new site&#x27;s navigation.</p>

<p>Source snapshot incomplete; excluded from the saved baseline.</p>

</details>

<h3>Getting Started and Basics — update</h3>

```diff
--- a/README.md
+++ b/README.md
@@ -219,7 +219,7 @@
 ## Go
 
  - [Awesome Go](https://github.com/avelino/awesome-go) - A curated list of awesome Go frameworks, libraries, software and resources.
- - [Getting Started and Basics](https://tour.golang.org/welcome) - Introduction to programming with Go.
+ - [Getting Started and Basics](https://go.dev/tour/welcome) - Introduction to programming with Go.
  - [JSON-to-Go](https://mholt.github.io/json-to-go/) - This tool instantly converts JSON into a Go type definition.
  - [YAML-to-Go](https://zhwt.github.io/yaml-to-go/) - This tool instantly converts YAML into a Go type definition.
 
```

<details>
<summary>Evidence and limitations</summary>

<p>tour.golang.org now redirects to the official go.dev domain. The content is still &#x27;A Tour of Go&#x27;, so the description holds. Only the URL needs updating to the canonical location.</p>

<p>https://go.dev/tour/welcome — https://tour.golang.org/welcome redirects (1 hop) to this URL, which returns HTTP 200 with the title &#x27;A Tour of Go&#x27;.</p>

<p>Caveats: The old URL still redirects correctly, so this is canonicalization rather than a fix for a broken link.</p>

</details>

<h3>Arista EAPI — update</h3>

<p>0 proposed change(s); 1 held for unresolved questions.</p>

<details>
<summary>Evidence and limitations</summary>

<p>The listed eos.arista.com URL now redirects to the generic Arista Community homepage, not the article. Search results show the &#x27;Arista eAPI 101&#x27; article migrated to the Arista Community article URL below, and its text matches the entry (&#x27;a simple and complete API that allows you to configure and monitor your Arista switches&#x27;). The description stays accurate; only the URL changes.</p>

<p>https://eos.arista.com/arista-eapi-101/ — Redirects (1 hop) to https://arista.my.site.com/AristaCommunity/s/, the community homepage, not the article.</p>

<p>https://arista.my.site.com/AristaCommunity/s/article/arista-eapi-101 — Returns HTTP 200 (Salesforce Experience page titled &#x27;Arista Community&#x27;). The body is client-rendered and could not be read with curl or WebFetch. Search-index results list this URL as &#x27;Arista eAPI 101&#x27; (Addison Chi, 2014), containing the description sentence and covering enabling &#x27;management api http-commands&#x27;.</p>

<p>Blocking questions: The new article URL&#x27;s body could not be read directly (client-side rendering). Its identity is confirmed only by a 200 response and search-index title/snippets. A maintainer should open it in a browser before applying.</p>

<p>Caveats: The article dates from 2014 but still describes the eAPI enablement flow. It is historic and remains useful.</p>

</details>

<h3>Cisco DNA Center Platform API — update</h3>

```diff
--- a/README.md
+++ b/README.md
@@ -226,7 +226,7 @@
 ## Vendor API Docs
 
  - [Arista EAPI](https://eos.arista.com/arista-eapi-101/) - The Arista Command eAPI is a simple and complete API that allows you to configure and monitor your Arista switches.
- - [Cisco DNA Center Platform API](https://developer.cisco.com/docs/dna-center/) - Online documentation of Cisco DNA Center Platform API.
+ - [Cisco Catalyst Center Platform API](https://developer.cisco.com/docs/catalyst-center/) - Online documentation of Cisco Catalyst Center (formerly DNA Center) Platform API.
  - [Cisco IOS XE CSR1000V](https://www.cisco.com/c/en/us/td/docs/routers/csr1000/software/restapi/restapi/RESTAPIintro.html) - Cisco IOS XE REST API Management Reference Guide.
     - [IOS-XE Programmability](https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/prog/configuration/177/b_177_programmability_cg.html) - Documentation for Plug and Play, Guestshell, Python API, EEM, NETCONF, RESTCONF, gNMI/gNOI, gRPC and Application Hosting.
  - [Cisco IOS-XR](https://www.cisco.com/c/en/us/td/docs/ios_xr_sw/iosxr_r4-1/xml/programming/guide/xl41apidoc.html) - Cisco IOS-XR API Docs only.
```

<details>
<summary>Evidence and limitations</summary>

<p>Cisco renamed DNA Center to Catalyst Center. The listed URL redirects to the Catalyst Center API docs, which state that DNA Center is now Catalyst Center. The resource is still the platform/Intent API documentation and still fits. The name, URL and description should use the current product name.</p>

<p>https://developer.cisco.com/docs/catalyst-center/ — /docs/dna-center/ redirects here (HTTP 200). Title &#x27;Introduction - Cisco Catalyst Center API 3.1.6&#x27;. Page text: &#x27;Cisco DNA Center is now Catalyst Center… they refer to the same product.&#x27; It covers Intent API (Northbound), Events and Notifications, and Integration API.</p>

<p>Caveats: The API version shown (3.1.6) will change over time, so the suggested wording leaves it out.</p>

</details>

<h3>XR-Docs — update</h3>

```diff
--- a/README.md
+++ b/README.md
@@ -230,7 +230,7 @@
  - [Cisco IOS XE CSR1000V](https://www.cisco.com/c/en/us/td/docs/routers/csr1000/software/restapi/restapi/RESTAPIintro.html) - Cisco IOS XE REST API Management Reference Guide.
     - [IOS-XE Programmability](https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/prog/configuration/177/b_177_programmability_cg.html) - Documentation for Plug and Play, Guestshell, Python API, EEM, NETCONF, RESTCONF, gNMI/gNOI, gRPC and Application Hosting.
  - [Cisco IOS-XR](https://www.cisco.com/c/en/us/td/docs/ios_xr_sw/iosxr_r4-1/xml/programming/guide/xl41apidoc.html) - Cisco IOS-XR API Docs only.
-   - [XR-Docs](https://xrdocs.github.io) - Documentation Blogs and Tutorials on all things IOS-XR An Open, Extensible and Stable Cloud-Scale Network Operating System.
+   - [XR-Docs](https://xrdocs.io/) - Documentation Blogs and Tutorials on all things IOS-XR An Open, Extensible and Stable Cloud-Scale Network Operating System.
    - [NX_API Coming soon]() - Coming Soon.
    - [Cisco NX-API](https://developer.cisco.com/site/nx-api/) - Main DEVNET page for NX-API docs.
  - [Checkpoint Management API](https://sc1.checkpoint.com/documents/latest/APIs/#web/) - Checkpoint Management REST API docs.
```

<details>
<summary>Evidence and limitations</summary>

<p>xrdocs.github.io redirects to xrdocs.io. The site is active, with content dated through November 2026 on IOS XR automation, programmability and telemetry, so it still fits. Only the URL should change to the canonical domain; the description is still accurate.</p>

<p>https://xrdocs.io/ — https://xrdocs.github.io redirects (2 hops) here, HTTP 200. Title &#x27;XRdocs - Cisco IOS XR Documentation&#x27;. Meta description: &#x27;Technical documentation, tutorials, and blogs for Cisco IOS XR network engineers. Learn automation, telemetry, segment routing, programmability, and more.&#x27; Most recent dates on page: 2026-11-09.</p>

<p>Caveats: Optional: the description&#x27;s run-on wording could be tidied, but it is not factually wrong.</p>

</details>

<h3>F5 — update</h3>

```diff
--- a/README.md
+++ b/README.md
@@ -239,7 +239,7 @@
    - [EXOS REST API](https://github.com/extremenetworks/EXOS_Apps/tree/master/REST) - Documentation and examples for ExtremeSwitching ExtremeXOS RESTCONF API.
    - [EXOS JSONRPC Interface](https://github.com/extremenetworks/EXOS_Apps/tree/master/JSONRPC) - Documentation and examples for ExtremeSwitching ExtremeXOS JSONRPC API.
    - [EXOS Python API](https://api.extremenetworks.com/EXOS/ProgramInterfaces/PYTHONAPI/?_ga=2.86707664.93471558.1615766490-270125121.1613692686) - Documentation for writing Python applications that run on ExtremeXOS based switches.
- - [F5](https://devcentral.f5.com/d/icontrolr-rest-api-user-guide-version-1300-241) - REST API User Guide, Version 13.0.0.
+ - [F5](https://clouddocs.f5.com/api/icontrol-rest/) - BIG-IP iControl REST API reference and user guides.
  - [Infoblox Perl API](https://demogm1.infoblox.com/api/doc/) and [Infoblox REST API](https://demogm1.infoblox.com/wapidoc/)
  - IP Infusion OcNOS:
    - [OcNOS NETCONF User Manual](https://documentation.ipinfusion.com/ocnos-sp-netconf-user-manual-7.0/Default.htm) - NETCONF and YANG on OcNOS, including candidate datastore, confirmed commit and validate.
```

<details>
<summary>Evidence and limitations</summary>

<p>The DevCentral link for the 13.0.0 user guide now redirects to the generic F5 community homepage, so the listed document is no longer reachable there. F5&#x27;s official iControl REST home on CloudDocs is the current entry point for the BIG-IP REST API reference and user guides, including a 16.1+ guide. Recommend pointing to CloudDocs and dropping the volatile version number.</p>

<p>https://devcentral.f5.com/d/icontrolr-rest-api-user-guide-version-1300-241 — Redirects (1 hop) to https://community.f5.com/, the generic homepage, not the guide.</p>

<p>https://clouddocs.f5.com/api/icontrol-rest/ — HTTP 200, &#x27;iControl REST Home&#x27;. Entry point to the BIG-IP iControl REST API reference (LTM, GTM, Security, etc.). Links &#x27;iControl REST User Guide Version 16.1+&#x27; (PDF on community.f5.com) and an AFM REST guide (11.6).</p>

<p>Caveats: Search results suggest CloudDocs may also list older version-specific PDFs, including 13.0, but my fetch of the page only surfaced the 16.1+, AVR and AFM PDF links. A version-specific 13.0 link was not confirmed.</p>

</details>

<h3>IOS-XE Programmability — update</h3>

```diff
--- a/README.md
+++ b/README.md
@@ -228,7 +228,7 @@
  - [Arista EAPI](https://eos.arista.com/arista-eapi-101/) - The Arista Command eAPI is a simple and complete API that allows you to configure and monitor your Arista switches.
  - [Cisco DNA Center Platform API](https://developer.cisco.com/docs/dna-center/) - Online documentation of Cisco DNA Center Platform API.
  - [Cisco IOS XE CSR1000V](https://www.cisco.com/c/en/us/td/docs/routers/csr1000/software/restapi/restapi/RESTAPIintro.html) - Cisco IOS XE REST API Management Reference Guide.
-    - [IOS-XE Programmability](https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/prog/configuration/177/b_177_programmability_cg.html) - Documentation for Plug and Play, Guestshell, Python API, EEM, NETCONF, RESTCONF, gNMI/gNOI, gRPC and Application Hosting.
+    - [IOS-XE Programmability](https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/prog/configuration/177/b_177_programmability_cg.html) - Documentation for Zero-Touch Provisioning, iPXE, Guest Shell, Python API, EEM, NETCONF, RESTCONF, gNMI/gNOI, Model-Driven Telemetry and Application Hosting.
  - [Cisco IOS-XR](https://www.cisco.com/c/en/us/td/docs/ios_xr_sw/iosxr_r4-1/xml/programming/guide/xl41apidoc.html) - Cisco IOS-XR API Docs only.
    - [XR-Docs](https://xrdocs.github.io) - Documentation Blogs and Tutorials on all things IOS-XR An Open, Extensible and Stable Cloud-Scale Network Operating System.
    - [NX_API Coming soon]() - Coming Soon.
```

<details>
<summary>Evidence and limitations</summary>

<p>The 17.7.x Programmability Configuration Guide is reachable and still fits. However, its table of contents has no Plug and Play chapter. It lists Zero-Touch Provisioning and iPXE instead, along with Guest Shell, Python API, EEM Python Module, NETCONF, RESTCONF, gNMI, gNOI, Model-Driven Telemetry and Application Hosting. The description should drop the unsupported Plug and Play claim.</p>

<p>https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/prog/configuration/177/b_177_programmability_cg.html — &#x27;Programmability Configuration Guide, Cisco IOS XE Cupertino 17.7.x&#x27;, last updated December 7, 2021. TOC: Zero-Touch Provisioning, iPXE, Guest Shell, Python API, EEM Python Module, NETCONF Protocol, RESTCONF Protocol, NETCONF and RESTCONF Service-Level ACLs, gNMI Protocol, gRPC Network Operations Interface, Model Based AAA, Model-Driven Telemetry, In-Service Model Update, Application Hosting. No &#x27;Plug and Play&#x27; or &#x27;PnP&#x27; in the page text.</p>

<p>Caveats: Page content was read via WebFetch, since direct curl got HTTP 403 from cisco.com.; Newer IOS XE programmability guides exist. Optionally the maintainer could point to a newer release, but the 17.7 guide is still valid documentation.</p>

<p>Source snapshot incomplete; excluded from the saved baseline.</p>

</details>

<h3>NX_API Coming soon — remove</h3>

<p>0 proposed change(s); 1 held for unresolved questions.</p>

<details>
<summary>Evidence and limitations</summary>

<p>This is an empty placeholder (&#x27;[NX_API Coming soon]()&#x27; – &#x27;Coming Soon.&#x27;) with no link, present since a 2017 re-org. The very next line already provides the real Cisco NX-API resource (DevNet NX-API page, which is live). There is no resource to evaluate, and the placeholder adds nothing. The entry is marked non-editable, so a maintainer would need to remove it by hand.</p>

<p>https://github.com/networktocode/awesome-network-automation/blob/2a170d9f6ba7e9b4e16ec6639913c4edcecda8d8/README.md — README line 234 is &#x27;   - [NX_API Coming soon]() - Coming Soon.&#x27; with an empty link target. Line 235 is the real &#x27;[Cisco NX-API](https://developer.cisco.com/site/nx-api/)&#x27; entry. git log -S shows the placeholder dates back to commit c53b1ae (2017-09-21, &#x27;minor re-org&#x27;).</p>

<p>https://developer.cisco.com/site/nx-api/ — The sibling NX-API DevNet page is live (HTTP 200) and covers the NX-API docs this placeholder anticipated.</p>

<p>Caveats: This is based on repository content, not on vendor evidence. No external resource exists for this entry.</p>

<p>Source snapshot incomplete; excluded from the saved baseline.</p>

</details>

<h3>Cumulus Networks HTTP API — replace</h3>

<p>0 proposed change(s); 1 held for unresolved questions.</p>

<details>
<summary>Evidence and limitations</summary>

<p>The listed URL redirects to docs.nvidia.com and returns 404; the HTTP API page no longer exists in current Cumulus Linux docs. The archived 4.4 docs show the HTTP API was &#x27;an HTTP application programming interface to NCLU&#x27;. NVIDIA&#x27;s 5.0 What&#x27;s New states &#x27;Cumulus Linux 5.0.0 replaces NCLU with the NVUE object model&#x27;, and current docs describe the NVUE REST API as functionally equivalent to the NVUE CLI. The documented REST API for current Cumulus Linux is the NVUE API page. An alternative that keeps the history is pointing to the archived 4.4 HTTP API page (also live).</p>

<p>https://docs.cumulusnetworks.com/cumulus-linux/System-Configuration/HTTP-API/ — Redirects to https://docs.nvidia.com/networking-ethernet-software/cumulus-linux/System-Configuration/HTTP-API/, which returns HTTP 404.</p>

<p>https://docs.nvidia.com/networking-ethernet-software/cumulus-linux-44/System-Configuration/HTTP-API/ — &#x27;HTTP API | Cumulus Linux 4.4&#x27; (HTTP 200): &#x27;Cumulus Linux implements an HTTP application programming interface to NCLU&#x27;, served by the restserver service via nginx on port 8080.</p>

<p>https://docs.nvidia.com/networking-ethernet-software/cumulus-linux-50/Whats-New/ — &#x27;Cumulus Linux 5.0.0 replaces NCLU with the NVUE object model.&#x27; Also: &#x27;Cumulus Linux 3.7, 4.3, and 4.4 releases continue to support NCLU.&#x27;</p>

<p>https://docs.nvidia.com/networking-ethernet-software/cumulus-linux/System-Configuration/NVIDIA-User-Experience-NVUE/NVUE-API/ — &#x27;NVUE API | Cumulus Linux 5.18&#x27; (HTTP 200). Documents the NVUE REST API (nvue_v1 on port 8765) with GET/POST/PATCH/DELETE and revision-based config changes.</p>

<p>Blocking questions: NVIDIA&#x27;s docs say NVUE replaces NCLU, and the HTTP API was an interface to NCLU, but I found no sentence that names the NVUE REST API as the HTTP API&#x27;s successor. A maintainer may prefer updating to the archived 4.4 HTTP API URL instead of replacing.</p>

<p>Caveats: The NVUE API is newer and differs in design from the NCLU HTTP API. Cumulus Linux 3.7, 4.3 and 4.4 still support NCLU, so the archived 4.4 page remains valid history.</p>

<p>Source snapshot incomplete; excluded from the saved baseline.</p>

</details>

<h3>EXOS Python API — update</h3>

```diff
--- a/README.md
+++ b/README.md
@@ -238,7 +238,7 @@
  - Extreme Networks:
    - [EXOS REST API](https://github.com/extremenetworks/EXOS_Apps/tree/master/REST) - Documentation and examples for ExtremeSwitching ExtremeXOS RESTCONF API.
    - [EXOS JSONRPC Interface](https://github.com/extremenetworks/EXOS_Apps/tree/master/JSONRPC) - Documentation and examples for ExtremeSwitching ExtremeXOS JSONRPC API.
-   - [EXOS Python API](https://api.extremenetworks.com/EXOS/ProgramInterfaces/PYTHONAPI/?_ga=2.86707664.93471558.1615766490-270125121.1613692686) - Documentation for writing Python applications that run on ExtremeXOS based switches.
+   - [EXOS Python API](https://documentation.extremenetworks.com/exos/api/ProgramInterfaces/PYTHONAPI/) - Documentation for writing Python applications that run on ExtremeXOS based switches.
  - [F5](https://devcentral.f5.com/d/icontrolr-rest-api-user-guide-version-1300-241) - REST API User Guide, Version 13.0.0.
  - [Infoblox Perl API](https://demogm1.infoblox.com/api/doc/) and [Infoblox REST API](https://demogm1.infoblox.com/wapidoc/)
  - IP Infusion OcNOS:
```

<details>
<summary>Evidence and limitations</summary>

<p>The listed api.extremenetworks.com URL (with Google Analytics tracking parameters) now redirects to an Extreme community hub that returns 403. The same EXOS Python API documentation is live on Extreme&#x27;s official documentation domain, and its content matches the description (native Python applications running on EXOS via &#x27;from exos import api&#x27;). Update the URL and drop the tracking parameters.</p>

<p>https://api.extremenetworks.com/EXOS/ProgramInterfaces/PYTHONAPI/ — Redirects (2 hops) to https://community.extremenetworks.com/t5/extreme-developer-center/ct-p/Extreme_Developer_Center, which returns HTTP 403. The same happens for other api.extremenetworks.com paths.</p>

<p>https://documentation.extremenetworks.com/exos/api/ProgramInterfaces/PYTHONAPI/ — HTTP 200. Title &#x27;The EXOS Python API — EXOS_Python documentation&#x27;. &#x27;The EXOS Python API provides a high-level interface to EXOS functionality. It is part of the EXOS SDK, which allows third-parties and customers to develop native applications which extend the functionality of EXOS… from exos import api.&#x27;</p>

<p>Caveats: The 403 on the community hub may be bot filtering, but the redirect target is no longer the documentation page either way.</p>

<p>Source snapshot incomplete; excluded from the saved baseline.</p>

</details>

<h3>Juniper JUNOS API — update</h3>

```diff
--- a/README.md
+++ b/README.md
@@ -244,7 +244,7 @@
  - IP Infusion OcNOS:
    - [OcNOS NETCONF User Manual](https://documentation.ipinfusion.com/ocnos-sp-netconf-user-manual-7.0/Default.htm) - NETCONF and YANG on OcNOS, including candidate datastore, confirmed commit and validate.
    - [OcNOS Streaming Telemetry Guide](https://documentation.ipinfusion.com/ocnos-sp-streaming-telemetry-7.0/Default.htm) - gNMI dial-in and dial-out telemetry with OpenConfig and native YANG models.
- - [Juniper JUNOS API](https://www.juniper.net/documentation/en_US/junos/information-products/pathway-pages/rest-api/rest-api.html) - JUNOS REST API Guide.
+ - [Juniper JUNOS API](https://networkingdocs.hpe.com/documentation/us/en/software/junos/rest-api/index.html) - JUNOS REST API Guide.
  - [Meraki Dashboard API](https://dashboard.meraki.com/api_docs) - Manage network environments within Meraki's cloud management tools.
    - [Meraki Dashboard API What's New](https://create.meraki.io/whats-new/) - Documentation of changes to API endpoints.
  - [Palo Alto Networks PAN-OS API](https://www.paloaltonetworks.com/documentation/80/pan-os/xml-api) - PAN-OS 8.0 XML API Reference.
```

<details>
<summary>Evidence and limitations</summary>

<p>The juniper.net URL now redirects to HPE Networking Documentation, following HPE&#x27;s acquisition of Juniper. The destination is still the Junos OS &#x27;REST API Guide&#x27; and sets its canonical link on networkingdocs.hpe.com. The description stays accurate and the fit is unchanged, so this is a URL-only correction to the resolved canonical location.</p>

<p>https://www.juniper.net/documentation/en_US/junos/information-products/pathway-pages/rest-api/rest-api.html — HTTP redirect resolves to https://networkingdocs.hpe.com/documentation/us/en/software/junos/rest-api/index.html (200).</p>

<p>https://networkingdocs.hpe.com/documentation/us/en/software/junos/rest-api/index.html — Title &#x27;REST API Guide | Junos OS | Juniper Networks&#x27;. Text: &#x27;The Junos OS REST API is a Representational State Transfer (REST) interface that enables you to securely connect to Junos OS devices, execute remote procedure calls, use a REST API Explorer...&#x27;. Its canonical-link script points to the networkingdocs.hpe.com host. The site is labelled &#x27;HPE Juniper Networking Documentation&#x27;.</p>

<p>Caveats: The old juniper.net URL still works through the redirect, so keeping it would not break the link; the update only removes the redirect hop.</p>

</details>

<h3>Meraki Dashboard API — update</h3>

```diff
--- a/README.md
+++ b/README.md
@@ -245,7 +245,7 @@
    - [OcNOS NETCONF User Manual](https://documentation.ipinfusion.com/ocnos-sp-netconf-user-manual-7.0/Default.htm) - NETCONF and YANG on OcNOS, including candidate datastore, confirmed commit and validate.
    - [OcNOS Streaming Telemetry Guide](https://documentation.ipinfusion.com/ocnos-sp-streaming-telemetry-7.0/Default.htm) - gNMI dial-in and dial-out telemetry with OpenConfig and native YANG models.
  - [Juniper JUNOS API](https://www.juniper.net/documentation/en_US/junos/information-products/pathway-pages/rest-api/rest-api.html) - JUNOS REST API Guide.
- - [Meraki Dashboard API](https://dashboard.meraki.com/api_docs) - Manage network environments within Meraki's cloud management tools.
+ - [Meraki Dashboard API](https://developer.cisco.com/meraki/api-v1/) - Manage network environments within Meraki's cloud management tools.
    - [Meraki Dashboard API What's New](https://create.meraki.io/whats-new/) - Documentation of changes to API endpoints.
  - [Palo Alto Networks PAN-OS API](https://www.paloaltonetworks.com/documentation/80/pan-os/xml-api) - PAN-OS 8.0 XML API Reference.
 
```

<details>
<summary>Evidence and limitations</summary>

<p>dashboard.meraki.com/api_docs redirects to the official Cisco Meraki Developer Hub API v1 docs, which declare themselves canonical. The description (managing networks through Meraki&#x27;s cloud dashboard API) is still accurate. Recommend a URL-only correction to the canonical destination.</p>

<p>https://dashboard.meraki.com/api_docs — Redirects to https://developer.cisco.com/meraki/api-v1/ (200).</p>

<p>https://developer.cisco.com/meraki/api-v1/ — Title &#x27;Introduction - Meraki Dashboard API v1 - Cisco Meraki Developer Hub&#x27;. Canonical is https://developer.cisco.com/meraki/api-v1/. Meta description: &#x27;Leverage the Meraki Dashboard APIs to build custom networking solutions...&#x27;.</p>

</details>

<h3>Meraki Dashboard API What&#x27;s New — update</h3>

```diff
--- a/README.md
+++ b/README.md
@@ -246,7 +246,7 @@
    - [OcNOS Streaming Telemetry Guide](https://documentation.ipinfusion.com/ocnos-sp-streaming-telemetry-7.0/Default.htm) - gNMI dial-in and dial-out telemetry with OpenConfig and native YANG models.
  - [Juniper JUNOS API](https://www.juniper.net/documentation/en_US/junos/information-products/pathway-pages/rest-api/rest-api.html) - JUNOS REST API Guide.
  - [Meraki Dashboard API](https://dashboard.meraki.com/api_docs) - Manage network environments within Meraki's cloud management tools.
-   - [Meraki Dashboard API What's New](https://create.meraki.io/whats-new/) - Documentation of changes to API endpoints.
+   - [Meraki Dashboard API What's New](https://developer.cisco.com/meraki/whats-new/) - Documentation of changes to API endpoints.
  - [Palo Alto Networks PAN-OS API](https://www.paloaltonetworks.com/documentation/80/pan-os/xml-api) - PAN-OS 8.0 XML API Reference.
 
  ## Git
```

<details>
<summary>Evidence and limitations</summary>

<p>create.meraki.io/whats-new/ redirects to the official Meraki Developer Hub &#x27;What&#x27;s New &amp; Changelog&#x27; page, which declares itself canonical. That page still documents API endpoint changes (2026 entries list added endpoints and OAuth scopes), so the description is accurate. Recommend a URL-only correction.</p>

<p>https://create.meraki.io/whats-new/ — Redirects to https://developer.cisco.com/meraki/whats-new/ (200).</p>

<p>https://developer.cisco.com/meraki/whats-new/ — Title &#x27;2026 - Meraki Portal What&#x27;s New &amp; Changelog&#x27;. Canonical is https://developer.cisco.com/meraki/whats-new/. Meta description: &#x27;Explore release-specific feature enhancements and endpoint updates for Meraki dashboard API.&#x27; The changelog lists endpoint additions such as getNetworkWirelessSsidTrafficShapingRules.</p>

<p>Caveats: The page title says &#x27;Meraki Portal What&#x27;s New&#x27; rather than &#x27;Dashboard API&#x27;, but the content is API endpoint changes.</p>

</details>

<h3>Arista Validated Designs — update</h3>

```diff
--- a/README.md
+++ b/README.md
@@ -268,7 +268,7 @@
 
 ## Arista
 
- - [Arista Validated Designs](https://avd.arista.com/stable/index.html) - AVD is an extensible data model that defines Arista’s Unified Cloud Network architecture as “code”.
+ - [Arista AVD (Architect, Validate, Deploy)](https://avd.arista.com/stable/) - AVD is an extensible data model that defines Arista’s Unified Cloud Network architecture as “code”.
  - [Arista Network Test Automation](https://anta.arista.com/stable/) - ANTA is a Python framework that automates tests for Arista devices.
 
 ## Batfish
```

<details>
<summary>Evidence and limitations</summary>

<p>The description is still verbatim official text. However, the official name is now &#x27;Arista AVD - Architect, Validate, Deploy&#x27;: both the stable docs (currently 6.5) and the GitHub README use that heading, and &#x27;Arista Validated Designs&#x27; no longer appears on the docs home page or in the README. The listed name is an outdated expansion of AVD, so I propose a rename. The URL is the documented stable alias (avd.arista.com/stable/index.html is a JavaScript redirect to ../6.5/index.html), so I propose the README&#x27;s canonical stable link.</p>

<p>https://avd.arista.com/stable/index.html — A JavaScript and meta-refresh redirect page to ../6.5/index.html.</p>

<p>https://avd.arista.com/6.5/index.html — Heading &#x27;Arista AVD - Architect, Validate, Deploy&#x27;. Text: &#x27;Arista AVD is an extensible data model that defines Arista&#x27;s Unified Cloud Network architecture as &quot;code&quot;.&#x27; The string &#x27;Arista Validated Designs&#x27; does not appear.</p>

<p>https://raw.githubusercontent.com/aristanetworks/avd/devel/README.md — Title &#x27;# Arista AVD - Architect, Validate, Deploy&#x27;. Same description sentence. Links Stable docs at https://avd.arista.com/stable/. &#x27;Validated Designs&#x27; appears 0 times.</p>

<p>https://galaxy.ansible.com/api/v3/plugin/ansible/content/published/collections/index/arista/avd/ — The arista.avd collection is not deprecated and was updated 2026-10-09 (highest version 6.5.0-dev1).</p>

<p>Caveats: I found no formal rename announcement. The name change comes from current official README and docs headings.; &#x27;Arista Validated Designs&#x27; may still be recognized informally, so the rename is optional wording hygiene.</p>

</details>

<h3>Home Page — update</h3>

```diff
--- a/README.md
+++ b/README.md
@@ -272,7 +272,7 @@
  - [Arista Network Test Automation](https://anta.arista.com/stable/) - ANTA is a Python framework that automates tests for Arista devices.
 
 ## Batfish
- - [Home Page](https://bit.ly/2R0Mefx) - Batfish.org home page with tutorials, talks and technical papers detailing the research behind Batfish.
+ - [Home Page](https://batfish.org/) - Batfish.org home page with tutorials, talks and technical papers detailing the research behind Batfish.
  - Getting Started with Batfish
     - [Documentation](https://batfish.readthedocs.io) - Getting Started Documentation for Batfish.
     - [Jupyter Notebook](https://github.com/batfish/pybatfish/tree/master/jupyter_notebooks) - Jupyter Notebooks showing how to use Batfish for configuration, ACL, routing, forwarding, etc... analysis.
```

<details>
<summary>Evidence and limitations</summary>

<p>The bit.ly shortlink resolves to batfish.org with NTC UTM parameters. batfish.org still offers tutorials, talks (e.g. NANOG75) and research papers (NSDI 2015, SIGCOMM 2016/2017/2018/2023), so the description is accurate. The site notes Batfish is now an AWS-managed open source project. Recommend replacing the opaque third-party shortener with the canonical destination; the description is unchanged.</p>

<p>https://bit.ly/2R0Mefx — Redirects to https://batfish.org/?utm_source=ntc&amp;utm_medium=wiki&amp;utm_campaign=opensource (200).</p>

<p>https://batfish.org/ — Title &#x27;Batfish - An open source network configuration analysis tool&#x27;. Has &#x27;Tutorials&#x27;, &#x27;Talk at NANOG75...&#x27;, &#x27;Papers that describe the technology&#x27; (NSDI 2015, SIGCOMM 2016/2017/2018) and &#x27;Papers that build on Batfish&#x27; (SIGCOMM 2023). Says it was originally developed at Microsoft Research, UCLA and USC, later maintained by Intentionet, and is now an AWS-managed open source project.</p>

<p>Caveats: The shortlink carries NTC UTM attribution, which maintainers may want to keep deliberately. If they do, the current link works and keep is acceptable.</p>

</details>

<h3>Palo Alto Networks PAN-OS API — update</h3>

```diff
--- a/README.md
+++ b/README.md
@@ -247,7 +247,7 @@
  - [Juniper JUNOS API](https://www.juniper.net/documentation/en_US/junos/information-products/pathway-pages/rest-api/rest-api.html) - JUNOS REST API Guide.
  - [Meraki Dashboard API](https://dashboard.meraki.com/api_docs) - Manage network environments within Meraki's cloud management tools.
    - [Meraki Dashboard API What's New](https://create.meraki.io/whats-new/) - Documentation of changes to API endpoints.
- - [Palo Alto Networks PAN-OS API](https://www.paloaltonetworks.com/documentation/80/pan-os/xml-api) - PAN-OS 8.0 XML API Reference.
+ - [Palo Alto Networks PAN-OS API](https://docs.paloaltonetworks.com/ngfw/api) - PAN-OS and Panorama XML and REST API documentation.
 
  ## Git
 
```

<details>
<summary>Evidence and limitations</summary>

<p>The listed URL now redirects to docs.paloaltonetworks.com/documentation/80/pan-os/xml-api, which returns 404. Wayback shows it was already a 301 in 2022 and 2024. PAN-OS 8.0 docs are no longer served at that path. Palo Alto Networks now publishes the PAN-OS XML (and REST) API documentation in an unversioned NGFW API guide, for example &#x27;PAN-OS XML API Request Types and Actions&#x27; covering PAN-OS 8.1 through 12.2. Recommend pointing to the current official guide and dropping the version-specific &#x27;8.0&#x27; claim.</p>

<p>https://www.paloaltonetworks.com/documentation/80/pan-os/xml-api — Redirects to https://docs.paloaltonetworks.com/documentation/80/pan-os/xml-api, which returns HTTP 404.</p>

<p>https://web.archive.org/cdx/search/cdx?url=paloaltonetworks.com/documentation/80/pan-os/xml-api&amp;output=json — Captures in 2022-12 and 2024-10 both show status 301.</p>

<p>https://docs.paloaltonetworks.com/ngfw/api/pan-os-xml-api-request-types-and-actions — Official page &#x27;PAN-OS XML API Request Types and Actions&#x27; (keygen, config, commit, op, report, log, import, export, user-id, version; set/edit/delete/rename/clone/move). It lists applicability to PAN-OS 12.2, 12.1, 11.2, 11.1, 11.0, 10.2, 10.1, 10.0, 9.1, 9.0 and 8.1.</p>

<p>https://docs.paloaltonetworks.com/ngfw/api — The guide root redirects to &#x27;API Authentication and Security&#x27;, which says &#x27;To use the API (XML or REST), you must enable the API...&#x27;.</p>

<p>https://docs.paloaltonetworks.com/pan-os/11-1/pan-os-panorama-api — A versioned &#x27;PAN-OS and Panorama API Usage Guide&#x27; also exists. Its subpages redirect into /ngfw/api/.</p>

<p>Caveats: The /ngfw/api root redirects to its first topic (API Authentication and Security) instead of an overview page. Maintainers could use the request-types page as the landing URL if preferred.; I did not find a public PAN-OS 8.0-specific XML API guide. 8.0 is end-of-life.</p>

<p>Source snapshot incomplete; excluded from the saved baseline.</p>

</details>

<h3>StackStorm Repository — update</h3>

```diff
--- a/README.md
+++ b/README.md
@@ -313,7 +313,7 @@
  - [Using Salt at scale](https://docs.saltstack.com/en/latest/topics/tutorials/intro_scale.html) - Using Salt at scale.
 
 ## StackStorm
- - [StackStorm Repository](https://github.com/StackStorm/st2) - StackStorm (aka "IFTTT for Ops") is event-driven automation commonly used for auto-remediation, security responses, facilitated troubleshooting, complex deployments, and more. Includes rules engine, workflow, 1800+ integrations, native ChatOps and so forth.
+ - [StackStorm Repository](https://github.com/StackStorm/st2) - StackStorm (aka "IFTTT for Ops") is event-driven automation commonly used for auto-remediation, security responses, facilitated troubleshooting, complex deployments, and more. Includes rules engine, workflow, integration packs via StackStorm Exchange, native ChatOps and so forth.
  - [StackStorm Installer](https://docs.stackstorm.com/install/index.html) - Ready to install StackStorm? Here’s an overview of how to get your system up and running.
  - [StackStorm Youtube](https://www.youtube.com/channel/UCColc5CuBJ8-1SnALnkDz8Q) - Various intro, marketing, interviews, and technical product talks.
  - [Stackstorm Docs](https://docs.stackstorm.com) - Documentation repository for latest version of StackStorm.
```

<details>
<summary>Evidence and limitations</summary>

<p>The canonical repo is StackStorm/st2 (no redirect, not archived), and the event-driven automation description is still accurate. However, the entry&#x27;s count &#x27;1800+ integrations&#x27; does not match current official metadata. The repo description says &#x27;160 integration packs with 6000+ actions&#x27;, and the StackStorm Exchange index lists 169 packs. The suggested wording drops the volatile count and keeps the rest of the line.</p>

<p>https://github.com/StackStorm/st2 — Repo description: &#x27;StackStorm (aka &quot;IFTTT for Ops&quot;) is event-driven automation for auto-remediation, incident responses, troubleshooting, deployments, and more for DevOps and SREs. Includes rules engine, workflow, 160 integration packs with 6000+ actions (see https://exchange.stackstorm.org) and ChatOps.&#x27;</p>

<p>https://raw.githubusercontent.com/StackStorm-Exchange/index/master/v1/index.json — The Exchange index lists 169 packs.</p>

<p>https://raw.githubusercontent.com/StackStorm/st2/master/README.md — &#x27;StackStorm is a platform for integration and automation across services and tools... taking actions in response to events.&#x27; Describes sensors, triggers, actions, rules, workflows, packs and ChatOps.</p>

<p>Caveats: Network-automation fit comes from StackStorm&#x27;s event-driven auto-remediation use, not from network-specific code in this repo.; Did not run the software.</p>

</details>

<h3>Managing a Cisco switch with Puppet — update</h3>

```diff
--- a/README.md
+++ b/README.md
@@ -295,7 +295,7 @@
 
 ## Puppet
 
- - [Managing a Cisco switch with Puppet](http://www.scottyob.com/2012/12/08/my-experiences-of-managing-a-cisco-switch-with-puppet/) - My experiences of managing a Cisco switch with Puppet.
+ - [Managing a Cisco switch with Puppet](https://www.scottyob.com/post/2012/ios-with-puppet/) - My experiences of managing a Cisco switch with Puppet.
 
 ## Salt
 
```

<details>
<summary>Evidence and limitations</summary>

<p>The old URL redirects to https and then returns 404. The same post (same title, date 8 Dec 2012, and opening text) is live on the author&#x27;s rebuilt site at /post/2012/ios-with-puppet/. It is a historic but relevant write-up on managing a Cisco switch with Puppet. Only the URL changes.</p>

<p>http://www.scottyob.com/2012/12/08/my-experiences-of-managing-a-cisco-switch-with-puppet/ — Redirects to https://www.scottyob.com/2012/12/08/... and returns HTTP 404.</p>

<p>https://www.scottyob.com/post/2012/ios-with-puppet/ — HTTP 200. Title &#x27;My experiences of managing a Cisco switch with Puppet&#x27;, dated Saturday 8th December, 2012. Opens &#x27;One recent pet gripe of mine has been having to add a new VLAN into our datacenter for our vSphere platform... proof of concept post about how we could be using puppet...&#x27;.</p>

<p>https://web.archive.org/web/20201126055810/https://www.scottyob.com/2012/12/08/my-experiences-of-managing-a-cisco-switch-with-puppet/ — The 2020 archive of the old URL has the same title and text, confirming the new URL hosts the same post.</p>

<p>Caveats: The content dates from 2012 and is historic; that is not a reason to remove it.</p>

<p>Source snapshot incomplete; excluded from the saved baseline.</p>

</details>

<h3>Salt in 10 minutes — update</h3>

```diff
--- a/README.md
+++ b/README.md
@@ -302,7 +302,7 @@
  - [Napalm-Salt Repository](https://github.com/napalm-automation/napalm-salt) - The NAPALM-Salt Repository.
  - [salt-nornir](https://github.com/dmulyalin/salt-nornir) - proxy minion to manage network with SaltStack and Nornir using Netmiko, NAPALM, Scrapli, Ncclient, PyGNMI, PyATS based plugins to name a few.
  - [salt-sproxy](https://github.com/mirceaulinic/salt-sproxy) - Salt plugin to automate the management and configuration of (network) devices at scale, without running (Proxy) Minions.
- - [Salt in 10 minutes](https://docs.saltstack.com/en/latest/topics/tutorials/walkthrough.html) - Salt in 10 minutes.
+ - [Salt in 10 minutes](https://docs.saltproject.io/en/latest/topics/tutorials/walkthrough.html) - Salt in 10 minutes.
  - [Salt high availability and fault tolerance](https://docs.saltstack.com/en/latest/topics/highavailability/index.html) - Salt high availability and fault tolerance.
  - [Salt RIPE-74](https://ripe74.ripe.net/presentations/18-RIPE-74-Network-automation-at-scale-up-and-running-in-60-minutes.pdf) - Event-driven network automation using Salt: up and running in 60 minutes.
  - [Salt 2016.11](https://docs.saltstack.com/en/develop/topics/releases/2016.11.0.html#network-automation-napalm) - Salt 2016.11 (Carbon) release notes.
```

<details>
<summary>Evidence and limitations</summary>

<p>docs.saltstack.com is now a GitHub Pages stub. Its root redirects via meta refresh to docs.saltproject.io, and deep links return 404. The same official page, &#x27;Salt in 10 Minutes&#x27;, is live at the equivalent docs.saltproject.io path.</p>

<p>https://docs.saltstack.com/en/latest/topics/tutorials/walkthrough.html — HTTP 404 (server GitHub.com).</p>

<p>https://docs.saltstack.com/ — Root page contains meta refresh to https://docs.saltproject.io/en/latest/contents.html.</p>

<p>https://docs.saltproject.io/en/latest/topics/tutorials/walkthrough.html — HTTP 200, title &#x27;Salt in 10 Minutes&#x27;.</p>

<p>Caveats: General Salt tutorial; network-automation fit comes from the Salt section context.</p>

<p>Source snapshot incomplete; excluded from the saved baseline.</p>

</details>

<h3>Salt high availability and fault tolerance — update</h3>

```diff
--- a/README.md
+++ b/README.md
@@ -303,7 +303,7 @@
  - [salt-nornir](https://github.com/dmulyalin/salt-nornir) - proxy minion to manage network with SaltStack and Nornir using Netmiko, NAPALM, Scrapli, Ncclient, PyGNMI, PyATS based plugins to name a few.
  - [salt-sproxy](https://github.com/mirceaulinic/salt-sproxy) - Salt plugin to automate the management and configuration of (network) devices at scale, without running (Proxy) Minions.
  - [Salt in 10 minutes](https://docs.saltstack.com/en/latest/topics/tutorials/walkthrough.html) - Salt in 10 minutes.
- - [Salt high availability and fault tolerance](https://docs.saltstack.com/en/latest/topics/highavailability/index.html) - Salt high availability and fault tolerance.
+ - [Salt high availability and fault tolerance](https://docs.saltproject.io/en/latest/topics/highavailability/index.html) - Salt high availability and fault tolerance.
  - [Salt RIPE-74](https://ripe74.ripe.net/presentations/18-RIPE-74-Network-automation-at-scale-up-and-running-in-60-minutes.pdf) - Event-driven network automation using Salt: up and running in 60 minutes.
  - [Salt 2016.11](https://docs.saltstack.com/en/develop/topics/releases/2016.11.0.html#network-automation-napalm) - Salt 2016.11 (Carbon) release notes.
  - [Salt 2017.7](https://docs.saltstack.com/en/develop/topics/releases/2017.7.0.html#network-automation) - Salt 2017.7 (Nitrogen) release notes.
```

<details>
<summary>Evidence and limitations</summary>

<p>The old docs.saltstack.com deep link returns 404 because the domain now only redirects its root to docs.saltproject.io. The same page, &#x27;High Availability Features in Salt&#x27;, is live at the equivalent docs.saltproject.io path.</p>

<p>https://docs.saltstack.com/en/latest/topics/highavailability/index.html — HTTP 404.</p>

<p>https://docs.saltproject.io/en/latest/topics/highavailability/index.html — HTTP 200, title &#x27;High Availability Features in Salt&#x27;.</p>

<p>https://docs.saltstack.com/ — Meta refresh to docs.saltproject.io.</p>

<p>Source snapshot incomplete; excluded from the saved baseline.</p>

</details>

<h3>Salt 2016.11 — update</h3>

```diff
--- a/README.md
+++ b/README.md
@@ -305,7 +305,7 @@
  - [Salt in 10 minutes](https://docs.saltstack.com/en/latest/topics/tutorials/walkthrough.html) - Salt in 10 minutes.
  - [Salt high availability and fault tolerance](https://docs.saltstack.com/en/latest/topics/highavailability/index.html) - Salt high availability and fault tolerance.
  - [Salt RIPE-74](https://ripe74.ripe.net/presentations/18-RIPE-74-Network-automation-at-scale-up-and-running-in-60-minutes.pdf) - Event-driven network automation using Salt: up and running in 60 minutes.
- - [Salt 2016.11](https://docs.saltstack.com/en/develop/topics/releases/2016.11.0.html#network-automation-napalm) - Salt 2016.11 (Carbon) release notes.
+ - [Salt 2016.11](https://docs.saltproject.io/en/latest/topics/releases/2016.11.0.html#network-automation-napalm) - Salt 2016.11 (Carbon) release notes.
  - [Salt 2017.7](https://docs.saltstack.com/en/develop/topics/releases/2017.7.0.html#network-automation) - Salt 2017.7 (Nitrogen) release notes.
  - [SaltStack fundamentals](https://docs.saltstack.com/en/getstarted/fundamentals/) - Getting Started Guide walks you through the fundamental concepts you need to learn as you start using SaltStack.
  - [SaltStack configuration management](https://docs.saltstack.com/en/getstarted/config/) - SaltStack Configuration Management.
```

<details>
<summary>Evidence and limitations</summary>

<p>The docs.saltstack.com &#x27;develop&#x27; URL returns 404. The official 2016.11.0 (Carbon) release notes are live on docs.saltproject.io, and the page still has the id &#x27;network-automation-napalm&#x27;, so the anchor still works. The release notes are historic but still relevant.</p>

<p>https://docs.saltstack.com/en/develop/topics/releases/2016.11.0.html — HTTP 404.</p>

<p>https://docs.saltproject.io/en/latest/topics/releases/2016.11.0.html — HTTP 200, title &#x27;Salt 2016.11.0 Release Notes - Codename Carbon&#x27;. HTML contains id=&quot;network-automation-napalm&quot;.</p>

<p>Caveats: Uses the &#x27;latest&#x27; docs tree rather than &#x27;develop&#x27;. Release-notes pages for old versions are kept in the latest tree.</p>

<p>Source snapshot incomplete; excluded from the saved baseline.</p>

</details>

<h3>Salt 2017.7 — update</h3>

```diff
--- a/README.md
+++ b/README.md
@@ -306,7 +306,7 @@
  - [Salt high availability and fault tolerance](https://docs.saltstack.com/en/latest/topics/highavailability/index.html) - Salt high availability and fault tolerance.
  - [Salt RIPE-74](https://ripe74.ripe.net/presentations/18-RIPE-74-Network-automation-at-scale-up-and-running-in-60-minutes.pdf) - Event-driven network automation using Salt: up and running in 60 minutes.
  - [Salt 2016.11](https://docs.saltstack.com/en/develop/topics/releases/2016.11.0.html#network-automation-napalm) - Salt 2016.11 (Carbon) release notes.
- - [Salt 2017.7](https://docs.saltstack.com/en/develop/topics/releases/2017.7.0.html#network-automation) - Salt 2017.7 (Nitrogen) release notes.
+ - [Salt 2017.7](https://docs.saltproject.io/en/latest/topics/releases/2017.7.0.html#network-automation) - Salt 2017.7 (Nitrogen) release notes.
  - [SaltStack fundamentals](https://docs.saltstack.com/en/getstarted/fundamentals/) - Getting Started Guide walks you through the fundamental concepts you need to learn as you start using SaltStack.
  - [SaltStack configuration management](https://docs.saltstack.com/en/getstarted/config/) - SaltStack Configuration Management.
  - [SaltStack Network Automation](https://docs.saltstack.com/en/develop/topics/network_automation/index.html) - SaltStack Network Automation Overview.
```

<details>
<summary>Evidence and limitations</summary>

<p>The docs.saltstack.com &#x27;develop&#x27; URL returns 404. The official 2017.7.0 (Nitrogen) release notes are live on docs.saltproject.io, and the page still has the id &#x27;network-automation&#x27;, so the anchor still works.</p>

<p>https://docs.saltstack.com/en/develop/topics/releases/2017.7.0.html — HTTP 404.</p>

<p>https://docs.saltproject.io/en/latest/topics/releases/2017.7.0.html — HTTP 200, title &#x27;Salt 2017.7.0 Release Notes - Codename Nitrogen&#x27;. HTML contains id=&quot;network-automation&quot;.</p>

<p>Source snapshot incomplete; excluded from the saved baseline.</p>

</details>

<h3>SaltStack Network Automation — update</h3>

```diff
--- a/README.md
+++ b/README.md
@@ -309,7 +309,7 @@
  - [Salt 2017.7](https://docs.saltstack.com/en/develop/topics/releases/2017.7.0.html#network-automation) - Salt 2017.7 (Nitrogen) release notes.
  - [SaltStack fundamentals](https://docs.saltstack.com/en/getstarted/fundamentals/) - Getting Started Guide walks you through the fundamental concepts you need to learn as you start using SaltStack.
  - [SaltStack configuration management](https://docs.saltstack.com/en/getstarted/config/) - SaltStack Configuration Management.
- - [SaltStack Network Automation](https://docs.saltstack.com/en/develop/topics/network_automation/index.html) - SaltStack Network Automation Overview.
+ - [SaltStack Network Automation](https://docs.saltproject.io/en/latest/topics/network_automation/index.html) - SaltStack Network Automation Overview.
  - [Using Salt at scale](https://docs.saltstack.com/en/latest/topics/tutorials/intro_scale.html) - Using Salt at scale.
 
 ## StackStorm
```

<details>
<summary>Evidence and limitations</summary>

<p>The docs.saltstack.com &#x27;develop&#x27; URL returns 404. The official Salt &#x27;Network Automation&#x27; overview page, which covers NAPALM-based network automation, is live at docs.saltproject.io.</p>

<p>https://docs.saltstack.com/en/develop/topics/network_automation/index.html — HTTP 404.</p>

<p>https://docs.saltproject.io/en/latest/topics/network_automation/index.html — HTTP 200, title &#x27;Network Automation&#x27;. The page includes a NAPALM section and NAPALM keywords.</p>

<p>Caveats: Uses the &#x27;latest&#x27; docs tree in place of the defunct &#x27;develop&#x27; path.</p>

<p>Source snapshot incomplete; excluded from the saved baseline.</p>

</details>

<h3>Using Salt at scale — update</h3>

```diff
--- a/README.md
+++ b/README.md
@@ -310,7 +310,7 @@
  - [SaltStack fundamentals](https://docs.saltstack.com/en/getstarted/fundamentals/) - Getting Started Guide walks you through the fundamental concepts you need to learn as you start using SaltStack.
  - [SaltStack configuration management](https://docs.saltstack.com/en/getstarted/config/) - SaltStack Configuration Management.
  - [SaltStack Network Automation](https://docs.saltstack.com/en/develop/topics/network_automation/index.html) - SaltStack Network Automation Overview.
- - [Using Salt at scale](https://docs.saltstack.com/en/latest/topics/tutorials/intro_scale.html) - Using Salt at scale.
+ - [Using Salt at scale](https://docs.saltproject.io/en/latest/topics/tutorials/intro_scale.html) - Using Salt at scale.
 
 ## StackStorm
  - [StackStorm Repository](https://github.com/StackStorm/st2) - StackStorm (aka "IFTTT for Ops") is event-driven automation commonly used for auto-remediation, security responses, facilitated troubleshooting, complex deployments, and more. Includes rules engine, workflow, 1800+ integrations, native ChatOps and so forth.
```

<details>
<summary>Evidence and limitations</summary>

<p>The old docs.saltstack.com deep link returns 404. The same official page, &#x27;Using Salt at scale&#x27;, is live at the equivalent docs.saltproject.io path.</p>

<p>https://docs.saltstack.com/en/latest/topics/tutorials/intro_scale.html — HTTP 404.</p>

<p>https://docs.saltproject.io/en/latest/topics/tutorials/intro_scale.html — HTTP 200, title &#x27;Using Salt at scale&#x27;.</p>

<p>Source snapshot incomplete; excluded from the saved baseline.</p>

</details>

<h3>StackStorm Intro on Software Gone Wild — update</h3>

```diff
--- a/README.md
+++ b/README.md
@@ -317,7 +317,7 @@
  - [StackStorm Installer](https://docs.stackstorm.com/install/index.html) - Ready to install StackStorm? Here’s an overview of how to get your system up and running.
  - [StackStorm Youtube](https://www.youtube.com/channel/UCColc5CuBJ8-1SnALnkDz8Q) - Various intro, marketing, interviews, and technical product talks.
  - [Stackstorm Docs](https://docs.stackstorm.com) - Documentation repository for latest version of StackStorm.
- - [StackStorm Intro on Software Gone Wild](https://blog.ipspace.net/2016/11/stackstorm-101-on-software-gone-wild.html) - SGW team talk with StackStorm (including Matt Oswalt) to discuss StackStorm.
+ - [StackStorm Intro on Software Gone Wild](https://blog.ipspace.net/2016/11/stackstorm-101-on-software-gone-wild/) - SGW team talk with StackStorm (including Matt Oswalt) to discuss StackStorm.
  
  ## SuzieQ
 
```

<details>
<summary>Evidence and limitations</summary>

<p>The 2016 podcast post is still live, and its content matches the description: a Software Gone Wild episode with Matt Oswalt, who had joined StackStorm, and Matt Stone, covering StackStorm sensors, actions, packs and networking uses. The listed .html URL now does a permanent redirect to a trailing-slash URL, so the only proposed change is the canonical URL. The description is accurate and the historic resource stays relevant.</p>

<p>https://blog.ipspace.net/2016/11/stackstorm-101-on-software-gone-wild.html — Redirects once to https://blog.ipspace.net/2016/11/stackstorm-101-on-software-gone-wild/ (HTTP 200).</p>

<p>https://blog.ipspace.net/2016/11/stackstorm-101-on-software-gone-wild/ — Post dated Friday, November 25, 2016, titled &quot;StackStorm 101 on Software Gone Wild&quot;. It says Matt Oswalt moved to the StackStorm team and Matt Stone joined; topics include sensors, actions, packs, and &quot;What can you do with StackStorm in networking today?&quot;. It links to Episode 67 of Software Gone Wild.</p>

<p>Caveats: I did not check the linked episode audio itself; this is a historic 2016 resource.</p>

</details>

<h3>eNMS — update</h3>

```diff
--- a/README.md
+++ b/README.md
@@ -327,7 +327,7 @@
 
 ## Products
 
- - [eNMS](https://github.com/afourmy/eNMS) - A vendor-agnostic NMS for carrier-grade network visualization and network automation.
+ - [eNMS](https://github.com/eNMS-automation/eNMS) - A vendor-agnostic NMS for carrier-grade network visualization and network automation.
  - [Nautobot](https://github.com/nautobot/nautobot) - Nautobot is a Network Source of Truth and Network Automation Platform.
  - [netpalm](https://github.com/tbotnz/netpalm) - netpalm is a ReST broker and abstraction layer for NAPALM, Netmiko, NCCLIENT or a Python Script.
  - [NSoT](https://github.com/dropbox/nsot) - Network Source of Truth (NSoT) is a source of truth database and repository for tracking inventory and metadata of network entities to ease management and automation of network infrastructure.
```

<details>
<summary>Evidence and limitations</summary>

<p>github.com/afourmy/eNMS redirects to github.com/eNMS-automation/eNMS, which the GitHub metadata in the packet snapshot confirms as the canonical repository (not archived, default branch &quot;public&quot;). The project still offers network visualization (geographical view, network builder) and workflow-based network automation, so the description stays accurate. Only the URL changes; the name stays eNMS.</p>

<p>https://github.com/afourmy/eNMS — Redirects to https://github.com/eNMS-automation/eNMS (HTTP 200).</p>

<p>https://github.com/eNMS-automation/eNMS — Repository description: &quot;An enterprise-grade vendor-agnostic network automation platform.&quot; No archive banner.</p>

<p>https://raw.githubusercontent.com/eNMS-automation/eNMS/public/README.md — &quot;eNMS is a vendor-agnostic NMS designed for building workflow-based network automation solutions.&quot; Features include configuration management, Netmiko/NAPALM validation, Ansible, REST, workflows, scheduling, and a &quot;Network visualization&quot; section (world map, network builder).</p>

<p>Caveats: The project now calls itself &quot;enterprise-grade&quot; where the entry says &quot;carrier-grade&quot;. This is marketing wording rather than a demonstrably false claim; the maintainer may optionally adopt the official wording.</p>

</details>

<h3>NSoT — replace</h3>

<p>0 proposed change(s); 1 held for unresolved questions.</p>

<details>
<summary>Evidence and limitations</summary>

<p>dropbox/nsot is not archived, and its README matches the entry description verbatim. However, the official PyPI &quot;nsot&quot; project (2.11.0 to 2.14.2, released Feb to Mar 2026) now lists https://github.com/jathanism/nsot as its homepage and repository. That repository&#x27;s README says &quot;NSoT was originally created at Dropbox and is now maintained by Jathan McCollum&quot; and describes Python 3.10+ / Django 5.2 releases. Its description of NSoT is identical to the entry. The package&#x27;s own distribution metadata points to it as the maintained continuation, so a replacement URL is suggested, pending maintainer review.</p>

<p>https://github.com/dropbox/nsot — No archive banner. Description: &quot;Network Source of Truth is an open source IPAM and network inventory database&quot;.</p>

<p>https://raw.githubusercontent.com/dropbox/nsot/develop/README.rst — Text matches the entry description. Points to nsot.readthedocs.io and pynsot, with IRC on freenode. Contains no successor notice.</p>

<p>https://pypi.org/pypi/nsot/json — Latest version 2.14.2, uploaded 2026-03-27. project_urls Homepage and Repository are https://github.com/jathanism/nsot. Releases 2.11.0 to 2.14.2 date from Feb to Mar 2026.</p>

<p>https://github.com/jathanism/nsot — Repository description: &quot;Network Source of Truth - Fork of Dropbox&#x27;s original NSoT that has been updated for Python 3 and Django 5.x&quot;. Default branch is main.</p>

<p>https://raw.githubusercontent.com/jathanism/nsot/main/README.md — &quot;NSoT was originally created at Dropbox and is now maintained by Jathan McCollum.&quot; v2.0.0 notes: Django 5.2, DRF 3.16, Python 3.10+. Install with pip install nsot.</p>

<p>Blocking questions: The dropbox/nsot repository has no notice pointing to the jathanism fork. The succession evidence comes from the PyPI nsot project metadata and the fork&#x27;s own README, so the maintainer should confirm they accept this as an official successor rather than an independent fork.</p>

<p>Caveats: I could not check commit history through the GitHub API (rate-limited).</p>

</details>

<h3>Rundeck — update</h3>

```diff
--- a/README.md
+++ b/README.md
@@ -331,7 +331,7 @@
  - [Nautobot](https://github.com/nautobot/nautobot) - Nautobot is a Network Source of Truth and Network Automation Platform.
  - [netpalm](https://github.com/tbotnz/netpalm) - netpalm is a ReST broker and abstraction layer for NAPALM, Netmiko, NCCLIENT or a Python Script.
  - [NSoT](https://github.com/dropbox/nsot) - Network Source of Truth (NSoT) is a source of truth database and repository for tracking inventory and metadata of network entities to ease management and automation of network infrastructure.
- - [Rundeck](https://rundeck.org/) - Job scheduler and runbook (and Ansible playbook) automation.
+ - [Rundeck](https://www.rundeck.com/) - Job scheduler and runbook (and Ansible playbook) automation.
 
 ## Library
 
```

<details>
<summary>Evidence and limitations</summary>

<p>rundeck.org now redirects (2 hops) to https://www.rundeck.com/, the official &quot;Rundeck by PagerDuty&quot; site. That site still offers an OSS download, job scheduling, runbook automation and &quot;Ansible Orchestration — Orchestrate Ansible playbooks&quot;, so the description stays accurate. Only the URL changes.</p>

<p>https://rundeck.org/ — Redirects twice and ends at https://www.rundeck.com/ (HTTP 200).</p>

<p>https://www.rundeck.com/ — Title: &quot;Rundeck Runbook Automation&quot;, 6.3.0 release banner. Offers &quot;Download OSS&quot; and &quot;Built on Open Source&quot;. Lists &quot;Job scheduling and infrastructure management&quot; and &quot;Ansible Orchestration: Orchestrate Ansible playbooks with other automation.&quot;</p>

<p>Caveats: The site mixes commercial Runbook Automation with OSS Rundeck. The entry describes the open-source scheduler and runbook tool, which is still offered.</p>

</details>

<h3>ciscoconfparse — replace</h3>

```diff
--- a/README.md
+++ b/README.md
@@ -338,7 +338,7 @@
  - [Aerleon](https://github.com/aerleon/aerleon) - Multi-platform ACL generation system with plugin support, YAML-based config, and a Python API. Fork of Capirca.
  - [Capirca](https://github.com/google/capirca) - Multi-platform ACL generation system; can output Juniper/IOS/etc ACLs from the same policy.
  - [Cisco Genie Parsers](https://pubhub.devnetcloud.com/media/genie-feature-browser/docs/#/parsers) - Genie Parsers by Cisco
- - [ciscoconfparse](https://github.com/mpenning/ciscoconfparse) - Parse, Audit, Query, Build, and Modify Cisco IOS-style configurations.
+ - [ciscoconfparse2](https://github.com/mpenning/ciscoconfparse2) - Parse, Audit, Query, Build, and Modify Cisco IOS-style and JunOS-style configurations. Successor to ciscoconfparse.
  - [Cisco virl2_client](https://developer.cisco.com/docs/virl2-client/) - Documentation for the VIRL 2 (aka CML) API Client. Use this library to create Python scripts to interact with CML.
  - [EasySNMP](https://github.com/kamakazikamikaze/easysnmp) - Easy to use and very fast SNMP library that uses Net-SNMP.
  - [FreeZTP](https://github.com/PackeTsar/freeztp) - FreeZTP is an open-source Zero-Touch Provisioning system for Cisco IOS campus switches and routers.
```

<details>
<summary>Evidence and limitations</summary>

<p>The listed repository is archived (Mar 2, 2025). Its README states &quot;ciscoconfparse is End of Life&quot; and that ciscoconfparse2, released December 14, 2023, is the equivalent of version 2.0 and &quot;You should upgrade&quot;. This is an officially documented successor by the same author. ciscoconfparse2 is active (PyPI 0.9.18, 2026-05-17) and still parses, audits, queries, builds and modifies IOS-style (and now multi-vendor) configurations.</p>

<p>https://github.com/mpenning/ciscoconfparse — &quot;This repository has been archived by the owner on Mar 2, 2025. It is now read-only.&quot;</p>

<p>https://raw.githubusercontent.com/mpenning/ciscoconfparse/main/README.md — &quot;Important: ciscoconfparse2 — ciscoconfparse is End of Life. As of December 14, 2023 ciscoconfparse2 is released; this is equivalent to version 2.0 of ciscoconfparse... You should upgrade.&quot; It warns that some legacy APIs are deprecated.</p>

<p>https://raw.githubusercontent.com/mpenning/ciscoconfparse2/main/README.md — &quot;ciscoconfparse2 is the next generation of ciscoconfparse, which was the primary development package from 2007 until 2023.&quot; It handles multi-vendor configs (Arista, Cisco, F5, Juniper, Palo Alto).</p>

<p>https://pypi.org/pypi/ciscoconfparse2/json — Version 0.9.18, uploaded 2026-05-17. Summary: &quot;Parse, Audit, Query, Build, and Modify Cisco IOS-style and JunOS-style configs&quot;. Repository: https://github.com/mpenning/ciscoconfparse2.</p>

<p>Caveats: ciscoconfparse2 is not a fully drop-in API replacement; the original README says to test code before migrating. The archived v1 repository and PyPI package (1.9.52) remain available for legacy users. I found no evidence about whether v1 receives any maintenance, and none should be inferred.</p>

</details>

<h3>EasySNMP — update</h3>

```diff
--- a/README.md
+++ b/README.md
@@ -340,7 +340,7 @@
  - [Cisco Genie Parsers](https://pubhub.devnetcloud.com/media/genie-feature-browser/docs/#/parsers) - Genie Parsers by Cisco
  - [ciscoconfparse](https://github.com/mpenning/ciscoconfparse) - Parse, Audit, Query, Build, and Modify Cisco IOS-style configurations.
  - [Cisco virl2_client](https://developer.cisco.com/docs/virl2-client/) - Documentation for the VIRL 2 (aka CML) API Client. Use this library to create Python scripts to interact with CML.
- - [EasySNMP](https://github.com/kamakazikamikaze/easysnmp) - Easy to use and very fast SNMP library that uses Net-SNMP.
+ - [EasySNMP](https://github.com/easysnmp/easysnmp) - Easy to use and very fast SNMP library that uses Net-SNMP.
  - [FreeZTP](https://github.com/PackeTsar/freeztp) - FreeZTP is an open-source Zero-Touch Provisioning system for Cisco IOS campus switches and routers.
  - [gNMIc](https://gnmic.kmrd.dev) - gNMI CLI client and collector.
  - [Hierarchical Configuration](https://github.com/netdevops/hier_config) - Hierarchical Configuration is a Python library that is able to take a running configuration of a network device, compare it to its intended configuration, and build the remediation steps necessary bring a device into spec with its intended configuration.
```

<details>
<summary>Evidence and limitations</summary>

<p>github.com/kamakazikamikaze/easysnmp redirects to github.com/easysnmp/easysnmp, the canonical repository per GitHub metadata. It is archived (Aug 6, 2025), but archival alone is not a removal reason and no successor is documented. The README still describes a fast, Pythonic SNMP library based on Net-SNMP bindings, so the description is accurate. Only the URL changes.</p>

<p>https://github.com/kamakazikamikaze/easysnmp — Redirects to https://github.com/easysnmp/easysnmp.</p>

<p>https://github.com/easysnmp/easysnmp — &quot;This repository has been archived by the owner on Aug 6, 2025. It is now read-only.&quot; Description: &quot;A blazingly fast and Pythonic SNMP library based on the official Net-SNMP bindings&quot;.</p>

<p>https://raw.githubusercontent.com/easysnmp/easysnmp/test/README.rst — &quot;Easy SNMP is a fork of Net-SNMP Python Bindings that attempts to bring a more Pythonic interface... more than 4 times faster than PySNMP.&quot; No successor or deprecation notice found.</p>

<p>https://pypi.org/pypi/easysnmp/json — Latest easysnmp 0.2.6, uploaded 2022-07-16. Homepage is still the kamakazikamikaze URL.</p>

<p>Caveats: The repository is archived and the last PyPI release was 2022; compatibility with current Python/Net-SNMP versions was not tested. Archival is informational only.</p>

</details>

<h3>FreeZTP — update</h3>

<p>0 proposed change(s); 1 held for unresolved questions.</p>

<details>
<summary>Evidence and limitations</summary>

<p>PackeTsar/freeztp is canonical and not archived. Its README (v1.5.1) describes &quot;A Zero-Touch Provisioning system built for Cisco Catalyst switches&quot; using IOS AutoInstall, and the repository description says &quot;for Cisco IOS&quot;. The README does not mention routers. The entry&#x27;s &quot;campus switches and routers&quot; claim therefore isn&#x27;t supported by the official docs, so a narrower wording is suggested.</p>

<p>https://github.com/PackeTsar/freeztp — No redirect, no archive banner. Description: &quot;An Open-Source Zero-Touch Provisioning System for Cisco IOS.&quot; Default branch is latest.</p>

<p>https://raw.githubusercontent.com/PackeTsar/freeztp/latest/README.md — &quot;A Zero-Touch Provisioning system built for Cisco Catalyst switches.&quot; &quot;FreeZTP is a dynamic TFTP server built to automatically configure Cisco Catalyst switches upon first boot... using the &#x27;AutoInstall&#x27; feature built into Cisco IOS.&quot; The README never mentions routers. Documented version is v1.5.1.</p>

<p>Blocking questions: The README not mentioning routers is not affirmative evidence that routers are unsupported. The maintainer may prefer to keep the original wording if router support is confirmed elsewhere, for example in issues or wiki pages I did not check.</p>

<p>Caveats: I did not run the software. Cisco IOS AutoInstall exists on some routers as well, so router use may work in practice.</p>

</details>

<h3>gNMIc — update</h3>

```diff
--- a/README.md
+++ b/README.md
@@ -342,7 +342,7 @@
  - [Cisco virl2_client](https://developer.cisco.com/docs/virl2-client/) - Documentation for the VIRL 2 (aka CML) API Client. Use this library to create Python scripts to interact with CML.
  - [EasySNMP](https://github.com/kamakazikamikaze/easysnmp) - Easy to use and very fast SNMP library that uses Net-SNMP.
  - [FreeZTP](https://github.com/PackeTsar/freeztp) - FreeZTP is an open-source Zero-Touch Provisioning system for Cisco IOS campus switches and routers.
- - [gNMIc](https://gnmic.kmrd.dev) - gNMI CLI client and collector.
+ - [gNMIc](https://gnmic.openconfig.net/) - gNMI CLI client and collector.
  - [Hierarchical Configuration](https://github.com/netdevops/hier_config) - Hierarchical Configuration is a Python library that is able to take a running configuration of a network device, compare it to its intended configuration, and build the remediation steps necessary bring a device into spec with its intended configuration.
  - [inet-henge](https://github.com/codeout/inet-henge) - Generate d3.js based Network Diagram from JSON data.
  - [Jinja2](http://jinja.pocoo.org/) - A full-featured template engine for Python.
```

<details>
<summary>Evidence and limitations</summary>

<p>gnmic.kmrd.dev now redirects to https://gnmic.openconfig.net/, the official docs site for the openconfig/gnmic project, titled &quot;gNMIc — gNMI client and telemetry collector&quot;. The description &quot;gNMI CLI client and collector&quot; remains accurate. Only the URL changes.</p>

<p>https://gnmic.kmrd.dev — Redirects once to https://gnmic.openconfig.net/ (HTTP 200).</p>

<p>https://gnmic.openconfig.net/ — Title: &quot;gNMIc — gNMI client and telemetry collector&quot;. Links to openconfig/gnmic and has a Command reference, Subscriptions, and many outputs (Kafka, InfluxDB, Prometheus, NATS, etc.).</p>

<p>Caveats: The GitHub API was rate-limited, so repository metadata for openconfig/gnmic was not read directly.</p>

</details>

<h3>Jinja2 — update</h3>

```diff
--- a/README.md
+++ b/README.md
@@ -345,7 +345,7 @@
  - [gNMIc](https://gnmic.kmrd.dev) - gNMI CLI client and collector.
  - [Hierarchical Configuration](https://github.com/netdevops/hier_config) - Hierarchical Configuration is a Python library that is able to take a running configuration of a network device, compare it to its intended configuration, and build the remediation steps necessary bring a device into spec with its intended configuration.
  - [inet-henge](https://github.com/codeout/inet-henge) - Generate d3.js based Network Diagram from JSON data.
- - [Jinja2](http://jinja.pocoo.org/) - A full-featured template engine for Python.
+ - [Jinja2](https://jinja.palletsprojects.com/) - A full-featured template engine for Python.
  - [NAPALM](https://github.com/napalm-automation/napalm) - NAPALM (Network Automation and Programmability Abstraction Layer with Multivendor support) is a Python library that implements a set of functions to interact with different router vendor devices using a unified API.
  - [Need To Graph](https://github.com/dmulyalin/N2G) - A library to generate diagrams in yWorks GraphML, diagrams.net/draw.io or JSON formats using structured data or show commands output.
  - [netaddr](https://github.com/drkjam/netaddr) - Network address manipulation that supports a number of techniques (supernetting and subnetting).
```

<details>
<summary>Evidence and limitations</summary>

<p>http://jinja.pocoo.org/ now redirects to https://jinja.palletsprojects.com/en/stable/, the official Pallets docs. The description (&#x27;full-featured template engine for Python&#x27;) still matches the docs (&#x27;fast, expressive, extensible templating engine&#x27;). Only the URL needs updating to the canonical HTTPS host.</p>

<p>http://jinja.pocoo.org/ — curl -L ends at https://jinja.palletsprojects.com/en/stable/ with HTTP 200.</p>

<p>https://jinja.palletsprojects.com/en/stable/ — Jinja Documentation (3.1.x): &#x27;Jinja is a fast, expressive, extensible templating engine... code similar to Python syntax.&#x27;</p>

<p>Caveats: The project now calls itself &#x27;Jinja&#x27;, but the PyPI package is still Jinja2. Renaming the entry is optional and not needed.</p>

</details>

<h3>netaddr — update</h3>

```diff
--- a/README.md
+++ b/README.md
@@ -348,7 +348,7 @@
  - [Jinja2](http://jinja.pocoo.org/) - A full-featured template engine for Python.
  - [NAPALM](https://github.com/napalm-automation/napalm) - NAPALM (Network Automation and Programmability Abstraction Layer with Multivendor support) is a Python library that implements a set of functions to interact with different router vendor devices using a unified API.
  - [Need To Graph](https://github.com/dmulyalin/N2G) - A library to generate diagrams in yWorks GraphML, diagrams.net/draw.io or JSON formats using structured data or show commands output.
- - [netaddr](https://github.com/drkjam/netaddr) - Network address manipulation that supports a number of techniques (supernetting and subnetting).
+ - [netaddr](https://github.com/netaddr/netaddr) - Network address manipulation that supports a number of techniques (supernetting and subnetting).
  - [netip](https://github.com/yanet-platform/netip) - Fast IPv4/IPv6 address-set operations for Rust-based ACL and policy automation, with arbitrary masks, zero dependencies, and no allocator.
  - [Netmiko](https://github.com/ktbyers/netmiko) - Multi-vendor library to simplify Paramiko SSH connections to network devices.
  - [Netutils](https://github.com/networktocode/netutils) - A Python library that is a collection of functions that are used in the common network automation tasks.
```

<details>
<summary>Evidence and limitations</summary>

<p>https://github.com/drkjam/netaddr redirects to https://github.com/netaddr/netaddr. The README lists that GitHub URL as the official source repository. The description is still accurate: the README lists &#x27;supernetting and subnetting&#x27; among many address-manipulation features. Only the URL needs updating.</p>

<p>https://github.com/drkjam/netaddr — curl -L ends at https://github.com/netaddr/netaddr with HTTP 200.</p>

<p>https://raw.githubusercontent.com/netaddr/netaddr/HEAD/README.rst — &#x27;A Python library for representing and manipulating network addresses.&#x27; Feature list includes &#x27;supernetting and subnetting&#x27;. &#x27;Source code repository: https://github.com/netaddr/netaddr/&#x27;.</p>

<p>https://raw.githubusercontent.com/netaddr/netaddr/HEAD/pyproject.toml — name netaddr, description &#x27;A network address manipulation library for Python&#x27;.</p>

<p>Caveats: Fit is general network-address tooling of the kind widely used in automation. Status unchanged.</p>

</details>

<h3>ansible-mysql-query — update</h3>

```diff
--- a/README.md
+++ b/README.md
@@ -364,7 +364,7 @@
 ## Non-Core Ansible Modules
 
  - [ansible-junos-stdlib](https://github.com/Juniper/ansible-junos-stdlib) - Junos OS modules for Ansible.
- - [ansible-mysql-query](https://github.com/zauberpony/ansible-mysql-query) - Ansible module to modify MySQL database records.
+ - [ansible-mysql-query](https://github.com/elmarx/ansible-mysql-query) - Ansible module to modify MySQL database records.
  - [ara](https://github.com/openstack/ara) - Ansible Runtime Analysis.
  - [FortiManager-Ansible](https://github.com/networktocode/fortimanager-ansible) - Ansible module to work with FortiManager.
  - [genieacs-ansible](https://github.com/GeiserX/genieacs-ansible) - Ansible collection for GenieACS (TR-069 ACS) with a dynamic inventory of CPE devices and modules for device tasks, presets and provisions.
```

<details>
<summary>Evidence and limitations</summary>

<p>https://github.com/zauberpony/ansible-mysql-query redirects to https://github.com/elmarx/ansible-mysql-query, so the owner was renamed. The README still describes an Ansible module that sets values in or inserts records into MySQL tables, so the description is accurate. The URL should point to the canonical owner.</p>

<p>https://github.com/zauberpony/ansible-mysql-query — curl -L ends at https://github.com/elmarx/ansible-mysql-query with HTTP 200.</p>

<p>https://raw.githubusercontent.com/elmarx/ansible-mysql-query/HEAD/README.md — &#x27;Ansible module to set values in a mysql table, or insert records.&#x27; Still listed on Galaxy as zauberpony.mysql-query.</p>

<p>Caveats: Fit with network automation is weak: it manages MySQL records, not network devices. That is a maintainer judgment, and there is no evidence the project lost its purpose, so removal is not supported.; The README&#x27;s Python 2 references suggest an older codebase. Activity was not assessed and is not a removal criterion.</p>

</details>

<h3>ara — update</h3>

```diff
--- a/README.md
+++ b/README.md
@@ -365,7 +365,7 @@
 
  - [ansible-junos-stdlib](https://github.com/Juniper/ansible-junos-stdlib) - Junos OS modules for Ansible.
  - [ansible-mysql-query](https://github.com/zauberpony/ansible-mysql-query) - Ansible module to modify MySQL database records.
- - [ara](https://github.com/openstack/ara) - Ansible Runtime Analysis.
+ - [ara](https://github.com/ansible-community/ara) - ARA Records Ansible playbook runs and makes them easier to understand and troubleshoot.
  - [FortiManager-Ansible](https://github.com/networktocode/fortimanager-ansible) - Ansible module to work with FortiManager.
  - [genieacs-ansible](https://github.com/GeiserX/genieacs-ansible) - Ansible collection for GenieACS (TR-069 ACS) with a dynamic inventory of CPE devices and modules for device tasks, presets and provisions.
  - [Infoblox-Ansible](https://github.com/infobloxopen/infoblox-ansible) - Ansible module to work with Infoblox.
```

<details>
<summary>Evidence and limitations</summary>

<p>https://github.com/openstack/ara redirects to https://github.com/ansible-community/ara. The official site (ara.recordsansible.org) lists that GitHub URL under sameAs, and GitHub reports the repo is not a mirror. The project now expands the acronym as &#x27;ARA Records Ansible&#x27; and describes itself as recording Ansible runs for troubleshooting. &#x27;Ansible Runtime Analysis&#x27; is an outdated expansion.</p>

<p>https://github.com/openstack/ara — curl -L ends at https://github.com/ansible-community/ara with HTTP 200. Page metadata shows isMirror false and isArchived false.</p>

<p>https://raw.githubusercontent.com/ansible-community/ara/HEAD/README.md — &#x27;ARA Records Ansible and makes it easier to understand and troubleshoot.&#x27; Records ansible/ansible-playbook runs through a callback plugin. Results are available via CLI, REST API and web UI.</p>

<p>https://ara.recordsansible.org/ — Official site title &#x27;ARA Records Ansible&#x27;. sameAs includes https://github.com/ansible-community/ara.</p>

<p>https://codeberg.org/ansible-community/ara — HTTP 200. The README points issues, tags and contributor history to Codeberg.</p>

<p>Caveats: Development activity (issues, tags) appears to happen on Codeberg while GitHub remains official. Either host is defensible. I chose GitHub because the redirect and the official site point there.</p>

</details>

<h3>pandevice — update</h3>

```diff
--- a/README.md
+++ b/README.md
@@ -390,7 +390,7 @@
  - [Infoblox Python Module](https://github.com/infobloxopen/infoblox-client) - Python wrapper for REST API
  - [Infoblox Go Client](https://github.com/infobloxopen/infoblox-go-client) - Go wrapper for REST API
  - [pan-python](https://github.com/kevinsteves/pan-python) - Multi-tool set for Palo Alto Networks PAN-OS, Panorama, WildFire and AutoFocus.
- - [pandevice](https://github.com/PaloAltoNetworks/pan-os-python) - Device framework for interacting with Palo Alto Networks devices.
+ - [pan-os-python](https://github.com/PaloAltoNetworks/pan-os-python) - Device framework for interacting with Palo Alto Networks devices.
  - [pyeapi](https://github.com/arista-eosplus/pyeapi) - Python library for Arista EOS.
  - [pyfg](https://github.com/spotify/pyfg) - Python library for Fortinet.
  - [pyiosxr](https://github.com/fooelisa/pyiosxr) - Python library for Cisco IOSXR.
```

<details>
<summary>Evidence and limitations</summary>

<p>The URL is already correct, but the entry&#x27;s name &#x27;pandevice&#x27; is outdated. The official README says pan-os-python &#x27;is the evolution of the older pandevice package&#x27; and gives migration steps from pandevice. The repository and package are now named pan-os-python, and the description remains accurate.</p>

<p>https://raw.githubusercontent.com/PaloAltoNetworks/pan-os-python/develop/README.md — Section &#x27;Upgrade from pandevice&#x27;: &#x27;This pan-os-python package is the evolution of the older pandevice package&#x27;, with steps to uninstall pandevice and change imports from pandevice to panos.</p>

<p>https://github.com/PaloAltoNetworks/pan-os-python — Canonical og:url is https://github.com/PaloAltoNetworks/pan-os-python (HTTP 200). Repo description: &#x27;The PAN-OS SDK for Python ... help interact with Palo Alto Networks devices&#x27;.</p>

<p>Caveats: The description &#x27;Device framework for interacting with Palo Alto Networks devices.&#x27; is still accurate and was left unchanged.</p>

</details>

<h3>TD4a — update</h3>

```diff
--- a/README.md
+++ b/README.md
@@ -424,7 +424,7 @@
 
  - [J2Live - TTL255](https://j2live.ttl255.com/) - Online Jinja2 parser. Additional support for Ansible and Salt filters.
  - [Jinja 101](https://jinja101.infrastructureascode.ch/) - Online Jinja2 parser with Ansible, SaltStack and Stackstorm filter support. Jinja2 environment settings can be configured.
- - [TD4a](https://td4a.codethenetwork.com/) - Advanced online rendering tool.
+ - [TD4a](https://github.com/cidrblock/td4a) - Template designer for automation; browser-based Jinja2 renderer with Ansible filter support, self-hosted via container or pip.
  - [textfsm.nornir.tech](https://textfsm.nornir.tech/) - Online development tool for Jinja2 templates and more.
 
 ### TextFSM
```

<details>
<summary>Evidence and limitations</summary>

<p>The listed hosted instance no longer serves TD4A. Over HTTPS, the hostname presents a *.storage.googleapis.com certificate, which fails the name check. Over HTTP and with verification disabled, it returns Google Cloud Storage &#x27;NoSuchBucket – The specified bucket does not exist&#x27;. The official project, cidrblock/td4a (&#x27;Template designer for automation&#x27;), is reachable and still documents a self-hosted renderer via container image and pip (td4a 2.0.3). Its README still links the dead hosted URL. Pointing the entry to the official repo keeps the same resource reachable. The description should then say what TD4A is rather than calling it an &#x27;online&#x27; tool.</p>

<p>https://td4a.codethenetwork.com/ — HTTPS fails: the certificate is for *.storage.googleapis.com, not td4a.codethenetwork.com. HTTP returns 404 with GCS XML &lt;Code&gt;NoSuchBucket&lt;/Code&gt;, &#x27;The specified bucket does not exist.&#x27;</p>

<p>https://github.com/cidrblock/td4a — Returns 200 with no redirect. og:title is &#x27;cidrblock/td4a: Template designer for automation&#x27;.</p>

<p>https://raw.githubusercontent.com/cidrblock/td4a/master/README.md — &#x27;TD4A is a visual design aid for building and testing jinja2 templates. It will combine data in yaml format with a jinja2 template and render the output. All jinja2 filters are supported along with the filter plugins from Ansible version 2.9.12.&#x27; Installed via podman/docker (cidrblock/td4a) or pip. &#x27;Try it now&#x27; still links the dead hosted URL.</p>

<p>https://pypi.org/pypi/td4a/json — td4a 2.0.3, summary &#x27;A browser based jinja template renderer&#x27;, last upload 2020-08-19.</p>

<p>Caveats: The hosted demo could be restored if the GCS bucket is recreated. If it comes back, the maintainer may prefer the original URL.; The software was not run. Its last release is from 2020; age alone is not a concern.</p>

<p>Source snapshot incomplete; excluded from the saved baseline.</p>

</details>

<h3>QEMU — update</h3>

```diff
--- a/README.md
+++ b/README.md
@@ -443,7 +443,7 @@
  - [Docker](https://www.docker.com/) - Docker is a software technology providing operating system-level virtualization also known as containers, promoted by the company Docker, Inc.
  - [KVM](https://www.linux-kvm.org/page/Main_Page) - KVM (Kernel-based Virtual Machine) is a full virtualization solution build into the Linux Kernel
  - [Proxmox](https://www.proxmox.com/en/proxmox-ve) - Proxmox is an open source virtualization platform that provides an easy web interface (and REST API) for KVM and LXC.
- - [QEMU](https://www.qemu.org/) - QEMU is a generic and open source machine emulator and virtualizer. When using KVM, QEMU can virtualize x86, server and embedded PowerPC, 64-bit POWER, S390, 32-bit and 64-bit ARM, and MIPS guests.
+ - [QEMU](https://www.qemu.org/) - QEMU is a generic and open source machine emulator and virtualizer, providing full-system emulation and near-native virtualization with KVM and Xen.
  - [Vagrant](https://www.vagrantup.com/) - Vagrant enables users to create and configure lightweight, reproducible, and portable development environments.
  - [VirtualBox](https://www.virtualbox.org/) - VirtualBox is a powerful x86 and AMD64/Intel64 virtualization product for enterprise as well as home use.
  - [Vmware ESXi](https://www.vmware.com/products/esxi-and-esx.html) - VMware ESXi is a purpose-built bare-metal hypervisor that installs directly onto a physical server.
```

<details>
<summary>Evidence and limitations</summary>

<p>QEMU is still a generic, open source machine emulator and virtualizer, but the description&#x27;s fixed KVM guest list is out of date. QEMU&#x27;s official removed-features page shows 64-bit MIPS hosts removed in 11.1 and 32-bit MIPS in 10.2, which ends MIPS KVM guests in current releases. KVM on 32-bit Arm hosts was removed in 5.2. The current accelerator table also adds RISC-V. Durable wording taken from the homepage avoids this volatile architecture list.</p>

<p>https://www.qemu.org/ — Tagline: &quot;A generic and open source machine emulator and virtualizer&quot;. Features: full-system emulation, user-mode emulation, and &quot;Run KVM and Xen virtual machines with near native performance&quot;. The latest release is 11.1.3 (Oct 28, 2026).</p>

<p>https://www.qemu.org/docs/master/about/removed-features.html — Under Host Architectures: &quot;32-bit MIPS (removed in 10.2)&quot;, &quot;64-bit MIPS (removed in 11.1)&quot; and &quot;32-bit PPC (removed in 10.2)&quot;. Also: &quot;KVM guest support on 32-bit Arm hosts (removed in 5.2)&quot;.</p>

<p>https://www.qemu.org/docs/master/system/introduction.html — The Supported Accelerators table lists KVM on Linux for &quot;Arm, MIPS, PPC, RISC-V, s390x, x86&quot;. MIPS is still listed there, which conflicts with the removed-features page.</p>

<p>Caveats: The QEMU intro page&#x27;s accelerator table still lists MIPS for KVM, which looks like stale docs. The proposed wording avoids the architecture list either way.; I did not run QEMU.</p>

</details>

<h3>Vagrant — update</h3>

```diff
--- a/README.md
+++ b/README.md
@@ -444,7 +444,7 @@
  - [KVM](https://www.linux-kvm.org/page/Main_Page) - KVM (Kernel-based Virtual Machine) is a full virtualization solution build into the Linux Kernel
  - [Proxmox](https://www.proxmox.com/en/proxmox-ve) - Proxmox is an open source virtualization platform that provides an easy web interface (and REST API) for KVM and LXC.
  - [QEMU](https://www.qemu.org/) - QEMU is a generic and open source machine emulator and virtualizer. When using KVM, QEMU can virtualize x86, server and embedded PowerPC, 64-bit POWER, S390, 32-bit and 64-bit ARM, and MIPS guests.
- - [Vagrant](https://www.vagrantup.com/) - Vagrant enables users to create and configure lightweight, reproducible, and portable development environments.
+ - [Vagrant](https://developer.hashicorp.com/vagrant) - Vagrant enables users to create and configure lightweight, reproducible, and portable development environments.
  - [VirtualBox](https://www.virtualbox.org/) - VirtualBox is a powerful x86 and AMD64/Intel64 virtualization product for enterprise as well as home use.
  - [Vmware ESXi](https://www.vmware.com/products/esxi-and-esx.html) - VMware ESXi is a purpose-built bare-metal hypervisor that installs directly onto a physical server.
 
```

<details>
<summary>Evidence and limitations</summary>

<p>The listed URL permanently redirects (308) to HashiCorp&#x27;s developer site. The official page still describes Vagrant as creating reproducible, portable development environments and managing VM lifecycles, so only the URL needs to change.</p>

<p>https://www.vagrantup.com/ — Returns HTTP/2 308 with Location https://developer.hashicorp.com/vagrant.</p>

<p>https://developer.hashicorp.com/vagrant — &quot;Vagrant is the command line utility for managing the lifecycle of virtual machines... Use Vagrant to create and configure a reproducible and portable work environment.&quot;</p>

<p>Caveats: Licensing changes (BSL) and HCP Vagrant Registry were not assessed. Neither affects the description.</p>

</details>

<h3>Vmware ESXi — update</h3>

<p>0 proposed change(s); 1 held for unresolved questions.</p>

<details>
<summary>Evidence and limitations</summary>

<p>VMware&#x27;s official hardening guide confirms that VCF 9 renamed the hypervisor from ESXi back to ESX; 8.x releases keep the ESXi name. The listed URL 301-redirects through /products/cloud-infrastructure/esxi-and-esx and lands on the vSphere product page. I found no standalone ESXi page. The bare-metal hypervisor description remains accurate.</p>

<p>https://www.vmware.com/products/esxi-and-esx.html — Returns HTTP 301 to https://www.vmware.com/products/cloud-infrastructure/esxi-and-esx, which then redirects to https://www.vmware.com/products/cloud-infrastructure/vsphere (final HTTP 200).</p>

<p>https://github.com/vmware/vcf-security-and-compliance-guidelines/tree/main/security-configuration-hardening-guide/cloud-foundation/9.1 — README: &quot;With the release of VMware Cloud Foundation 9 the name of the VMware Hypervisor was changed from ESXi back to ESX... please consider both ESXi and ESX to be the same&quot;.</p>

<p>https://www.vmware.com/products/cloud-infrastructure/vsphere — Title &quot;VMware vSphere | Virtualization Technology&quot;. The body is rendered client-side, so I could not read text mentioning ESX from it.</p>

<p>Blocking questions: I could not read the client-rendered vSphere page to confirm it describes ESX/ESXi. The URL change rests on VMware&#x27;s own redirect chain, not on page content.; Renaming the entry to &quot;VMware ESX&quot; is a maintainer choice, because the 8.x line still uses the ESXi name.</p>

<p>Caveats: ESXi 8.x is still in use under the old name, so the description keeps a reference to ESXi.</p>

</details>

<h3>Container-Lab — update</h3>

```diff
--- a/README.md
+++ b/README.md
@@ -451,7 +451,7 @@
 # Network Emulators
 
  - [CML](https://www.cisco.com/c/en/us/products/cloud-systems-management/modeling-labs/index.html) - Cisco Modeling Labs (CML), which replaces VIRL, is a network emulator with both an API and GUI frontend.
- - [Container-Lab](https://github.com/srl-wim/container-lab) - Containerlab provides a framework for orchestrating networking labs with containers. It starts the containers, builds a virtual wiring between them to create lab topologies of users choice and manages labs lifecycle.
+ - [Containerlab](https://github.com/srl-labs/containerlab) - Containerlab provides a CLI for orchestrating and managing container-based networking labs. It starts the containers, builds a virtual wiring between them to create lab topologies of users choice and manages labs lifecycle.
  - [EVE-NG](http://www.eve-ng.com/) - The Emulated Virtual Environment for Network, Security and DevOps professionals.
  - [FakeNOS](https://fakenos.github.io/fakenos/) -  Simulate network operating systems in a programmatic and easy way.
 
```

<details>
<summary>Evidence and limitations</summary>

<p>The repository was renamed and moved: github.com/srl-wim/container-lab redirects to github.com/srl-labs/containerlab, and the project calls itself &quot;Containerlab&quot;. The README now describes it as a CLI rather than a framework. The rest of the description still matches the README nearly word for word.</p>

<p>https://github.com/srl-wim/container-lab — Redirects to https://github.com/srl-labs/containerlab (HTTP 200).</p>

<p>https://github.com/srl-labs/containerlab — og:title &quot;GitHub - srl-labs/containerlab: container-based networking labs&quot;. The project links to https://containerlab.dev for docs.</p>

<p>https://raw.githubusercontent.com/srl-labs/containerlab/main/README.md — &quot;Containerlab provides a CLI for orchestrating and managing container-based networking labs. It starts the containers, builds a virtual wiring between them to create lab topologies of users choice and manages labs lifecycle.&quot;</p>

<p>Caveats: The GitHub API was rate-limited, so I could not check the archived flag directly. The packet snapshot reports archived=false, default branch main.</p>

</details>

<h3>EVE-NG — update</h3>

```diff
--- a/README.md
+++ b/README.md
@@ -452,7 +452,7 @@
 
  - [CML](https://www.cisco.com/c/en/us/products/cloud-systems-management/modeling-labs/index.html) - Cisco Modeling Labs (CML), which replaces VIRL, is a network emulator with both an API and GUI frontend.
  - [Container-Lab](https://github.com/srl-wim/container-lab) - Containerlab provides a framework for orchestrating networking labs with containers. It starts the containers, builds a virtual wiring between them to create lab topologies of users choice and manages labs lifecycle.
- - [EVE-NG](http://www.eve-ng.com/) - The Emulated Virtual Environment for Network, Security and DevOps professionals.
+ - [EVE-NG](https://www.eve-ng.net/) - The Emulated Virtual Environment for Network, Security and DevOps professionals.
  - [FakeNOS](https://fakenos.github.io/fakenos/) -  Simulate network operating systems in a programmatic and easy way.
 
 
```

<details>
<summary>Evidence and limitations</summary>

<p>http://www.eve-ng.com/ permanently redirects (301) to https://www.eve-ng.net/. EVE-NG is still an active multivendor network emulation product (Professional release 7.4.0-2, 1 November 2026), so only the URL needs to change.</p>

<p>http://www.eve-ng.com/ — Returns HTTP 301 Moved Permanently with Location https://www.eve-ng.net/.</p>

<p>https://www.eve-ng.net/ — &quot;EVE-NG Professional Edition Latest Now: Release 7.4.0-2, 1 November, 2026... EVE-NG PRO is the first clientless multivendor network emulation software that empowers network and security professionals&quot;.</p>

<p>Caveats: The exact tagline &quot;Emulated Virtual Environment for Network, Security and DevOps professionals&quot; was not found in the homepage text I extracted, but the page content supports it.</p>

</details>

<h3>NetPilot — update</h3>

```diff
--- a/README.md
+++ b/README.md
@@ -458,7 +458,7 @@
 
  - [GNS3](https://www.gns3.com/) - Graphical Network Simulator-3.
  - [Mininet](http://mininet.org/) - Mininet creates a realistic virtual network, running real kernel, switch and application code, on a single machine (VM, cloud or native), in seconds, with a single command.
- - [NetPilot](https://netpilot.io) - AI agent that designs, builds, and validates multi-vendor network labs from a plain-English prompt. Deploys 9+ real NOSes and growing (Cisco, Juniper, Arista, Nokia, Palo Alto, Fortinet, Aruba) on containerlab-based cloud sandboxes with real device CLIs.
+ - [NetPilot](https://www.netpilot.io/) - AI agent that designs, builds, and validates multi-vendor network labs from a plain-English prompt, deploying real NOS images (Nokia SR Linux, FRR and Linux built in; Cisco, Juniper, Arista, Palo Alto, Fortinet, Aruba and others via bring-your-own-image) on containerlab-based cloud or on-prem sandboxes with real device CLIs.
  - [netlab](https://github.com/ipspace/netlab) - Brings infrastructure-as-code concepts to networking labs. You'll describe your high-level network topology and routing design in a YAML file, and the tools in this repository will create configs for VirtualBox/libvirt/containerlab, Ansible inventory, IPv4/v6 addressing, VLANs and VRFs, OSPF, EIGRP, IS-IS, BGP, BFD, MPLS, MPLS/VPN, VXLAN, EVPN and Segment Routing.
  - [UNetLab](https://www.routereflector.com/unetlab/) - Unified Networking Lab.
  - [VRNetLab](https://github.com/plajjan/vrnetlab) - Run your favourite virtual routers in docker for convenient labbing, development and testing.
```

<details>
<summary>Evidence and limitations</summary>

<p>NetPilot is still an AI agent that builds multi-vendor labs from plain-English prompts on containerlab, so it remains relevant. Two description claims are outdated. The site now says 17+ supported NOSes, not 9+. Commercial vendors (Cisco, Juniper, Arista, Palo Alto, Fortinet, Aruba and others) run through bring-your-own-image, while Nokia SR Linux, FRR and Linux are built in. The site also offers on-prem deployment. The URL permanently redirects (308) to the www host. The proposed description drops the volatile count.</p>

<p>https://netpilot.io — Returns HTTP/2 308 with Location https://www.netpilot.io/.</p>

<p>https://www.netpilot.io/ — Meta description: &quot;AI agent that designs, builds &amp; validates multi-vendor labs from a prompt on real CLIs (Nokia built in; Cisco/Juniper/Arista BYOI)&quot;.</p>

<p>https://www.netpilot.io/ — FAQ: &quot;Nokia SR Linux, FRR, and Linux are built in. Commercial NOSes (Cisco IOL, XRd..., Juniper cRPD, Juniper vJunos..., Arista cEOS, Palo Alto, Fortinet, Aruba AOS-CX, Dell SmartFabric OS10, and MikroTik RouterOS (CHR)) run via bring-your-own-image (BYOI)... That is 17+ supported network operating systems today&quot;. Also: &quot;Each lab runs in its own isolated containerlab instance in the cloud&quot;, and the site offers an on-prem option.</p>

<p>Caveats: This is a commercial vendor product. Vendor submissions are allowed under the contribution rules.; I did not create an account or run a lab.</p>

</details>

<h3>netlab — update</h3>

```diff
--- a/README.md
+++ b/README.md
@@ -459,7 +459,7 @@
  - [GNS3](https://www.gns3.com/) - Graphical Network Simulator-3.
  - [Mininet](http://mininet.org/) - Mininet creates a realistic virtual network, running real kernel, switch and application code, on a single machine (VM, cloud or native), in seconds, with a single command.
  - [NetPilot](https://netpilot.io) - AI agent that designs, builds, and validates multi-vendor network labs from a plain-English prompt. Deploys 9+ real NOSes and growing (Cisco, Juniper, Arista, Nokia, Palo Alto, Fortinet, Aruba) on containerlab-based cloud sandboxes with real device CLIs.
- - [netlab](https://github.com/ipspace/netlab) - Brings infrastructure-as-code concepts to networking labs. You'll describe your high-level network topology and routing design in a YAML file, and the tools in this repository will create configs for VirtualBox/libvirt/containerlab, Ansible inventory, IPv4/v6 addressing, VLANs and VRFs, OSPF, EIGRP, IS-IS, BGP, BFD, MPLS, MPLS/VPN, VXLAN, EVPN and Segment Routing.
+ - [netlab](https://github.com/ipspace/netlab) - Brings infrastructure-as-code concepts to networking labs. You'll describe your high-level network topology and routing design in a YAML file, and the tools in this repository will create configs for libvirt/containerlab, Ansible inventory, IPv4/v6 addressing, VLANs and VRFs, OSPF, EIGRP, IS-IS, BGP, BFD, MPLS, MPLS/VPN, VXLAN, EVPN and Segment Routing.
  - [UNetLab](https://www.routereflector.com/unetlab/) - Unified Networking Lab.
  - [VRNetLab](https://github.com/plajjan/vrnetlab) - Run your favourite virtual routers in docker for convenient labbing, development and testing.
 
```

<details>
<summary>Evidence and limitations</summary>

<p>netlab remains relevant and active (latest release 26.10), but one listed capability is no longer supported. The official providers doc says the virtualbox provider was removed: use netlab 26.06 or earlier for VirtualBox. Current providers are libvirt (via Vagrant), clab (containerlab) and external. The other listed capabilities (Ansible inventory, IPv4/v6 addressing, VLANs, VRFs, OSPF, EIGRP, IS-IS, BGP, BFD, MPLS, L3VPN, VXLAN, EVPN, SR-MPLS/SRv6) are all in the README.</p>

<p>https://raw.githubusercontent.com/ipspace/netlab/dev/docs/providers.md — Lists the libvirt, clab and external providers. Note: &quot;The virtualbox provider is no longer available. Use netlab release 26.06 or earlier if you want to use VirtualBox.&quot;</p>

<p>https://raw.githubusercontent.com/ipspace/netlab/dev/README.md — &quot;Create containerlab configuration file to run Docker containers or Vagrantfile configuration file for libvirt/KVM environment; Create Ansible inventory...; Configure IPv4, IPv6, ... VLANs, VRFs, VXLAN, ... BFD, OSPFv2, OSPFv3, EIGRP, IS-IS, BGP, ... MPLS, BGP-LU, L3VPN (VPNv4 + VPNv6), 6PE, EVPN, SR-MPLS, or SRv6&quot;. The latest release is 26.10.</p>

<p>https://github.com/ipspace/netlab — og:title &quot;GitHub - ipspace/netlab: Making virtual networking labs suck less&quot;. The canonical repo is unchanged.</p>

<p>Caveats: Versions 26.06 and earlier still support VirtualBox, but the current version does not.</p>

</details>

<h3>VRNetLab — update</h3>

```diff
--- a/README.md
+++ b/README.md
@@ -461,7 +461,7 @@
  - [NetPilot](https://netpilot.io) - AI agent that designs, builds, and validates multi-vendor network labs from a plain-English prompt. Deploys 9+ real NOSes and growing (Cisco, Juniper, Arista, Nokia, Palo Alto, Fortinet, Aruba) on containerlab-based cloud sandboxes with real device CLIs.
  - [netlab](https://github.com/ipspace/netlab) - Brings infrastructure-as-code concepts to networking labs. You'll describe your high-level network topology and routing design in a YAML file, and the tools in this repository will create configs for VirtualBox/libvirt/containerlab, Ansible inventory, IPv4/v6 addressing, VLANs and VRFs, OSPF, EIGRP, IS-IS, BGP, BFD, MPLS, MPLS/VPN, VXLAN, EVPN and Segment Routing.
  - [UNetLab](https://www.routereflector.com/unetlab/) - Unified Networking Lab.
- - [VRNetLab](https://github.com/plajjan/vrnetlab) - Run your favourite virtual routers in docker for convenient labbing, development and testing.
+ - [VRNetLab](https://github.com/vrnetlab/vrnetlab) - Run your favourite virtual routers in docker for convenient labbing, development and testing.
 
 # Network Simulators
 
```

<details>
<summary>Evidence and limitations</summary>

<p>The listed repo github.com/plajjan/vrnetlab is now a GitHub fork of srl-labs/vrnetlab, the Containerlab fork. Its README says it is &#x27;a fork of the original plajjan/vrnetlab project&#x27; and its tagline is &#x27;Make VM-based Network OSes run in Containerlab&#x27;. The original project is now at github.com/vrnetlab/vrnetlab. That README opens with exactly the listed description (&#x27;Run your favourite virtual routers in docker for convenient labbing, development and testing&#x27;) and had commits in 2026. Fit as a network emulator for automation testing is unchanged. Recommend pointing the entry at the original upstream and keeping the description.</p>

<p>https://github.com/plajjan/vrnetlab — The repo page shows &#x27;forked from srl-labs/vrnetlab&#x27; and the description &#x27;Make VM-based Network OSes run in Containerlab&#x27;. Its raw README says &#x27;This is a fork of the original plajjan/vrnetlab project&#x27; and sends readers to the upstream docs at github.com/vrnetlab/vrnetlab.</p>

<p>https://raw.githubusercontent.com/vrnetlab/vrnetlab/master/README.md — The README begins &#x27;vrnetlab - VR Network Lab ... Run your favourite virtual routers in docker for convenient labbing, development and testing.&#x27; This matches the catalog description word for word.</p>

<p>https://github.com/vrnetlab/vrnetlab/commits/master.atom — The commit feed shows a latest update on 2026-02-10. The repo is not archived.</p>

<p>https://github.com/srl-labs/vrnetlab — This is the actively developed Containerlab fork (commit feed updated 2026-11-09). Its README calls vrnetlab/vrnetlab &#x27;the upstream repo&#x27;.</p>

<p>Caveats: The GitHub API was rate-limited, so fork and owner details come from the HTML page and atom feeds, not API metadata.; The maintainer could instead choose srl-labs/vrnetlab, the more active Containerlab-focused fork. That would need a different description.</p>

</details>

<h3>Juniper WANDL — remove</h3>

```diff
--- a/README.md
+++ b/README.md
@@ -468,7 +468,6 @@
  - [Batfish](https://github.com/batfish/batfish) - Batfish provides a model-based simulation for multi-vendor networks, that enables routing, forwarding, security, compliance, and what-if scenario analysis of a network (or proposed change to a network).
  - [Cisco WAN Automation Engine](https://www.cisco.com/c/en/us/products/routers/wae-planning/index.html) - Cisco WAE, formerly known as Cariden MATE, provides a multi-vendor network simulation that enables capacity planning and what-if scenario analysis for carrier networks.
  - [Forward Networks](https://forwardnetworks.com) - Forward Enterprise documents, searches, verifies, and predicts the behavior of your network by creating an always-accurate software copy of your entire network infrastructure for both on-prem and cloud.
- - [Juniper WANDL](https://www.juniper.net/us/en/products-services/sdn/wandl/) - Juniper WANDL provides traffic engineering
 models that enable capacity planning, network optimization and what-if scenario analysis for carrier networks.
  - [SuzieQ](https://github.com/netenglabs/suzieq) - SuzieQ is a agentless, multi-vendor network observability application.
 
```

<details>
<summary>Evidence and limitations</summary>

<p>The listed URL redirects to Juniper&#x27;s &#x27;WANDL IP/MPLSView Dates &amp; Milestones&#x27; end-of-life page. Juniper&#x27;s official (now HPE-hosted) WANDL IP/MPLSView documentation archive says &#x27;Juniper WANDL IP/MPLSView solution has reached end-of-support (EOS)&#x27;. The listed product is therefore officially discontinued, and the link no longer describes an available traffic engineering product. I found no official Juniper statement naming a direct successor. NorthStar Planner and Paragon Planner are related Juniper planning products, but their succession from WANDL is not officially documented in sources I read, so replace is not supported.</p>

<p>https://www.juniper.net/us/en/products-services/sdn/wandl/ — Redirects (HTTP 200) to https://support.juniper.net/support/eol/product/wandl/, titled &#x27;WANDL IP/MPLSView Dates &amp; Milestones - Juniper Networks&#x27;.</p>

<p>https://networkingdocs.hpe.com/documentation/en_US/ip-mplsview6.4.0/topics/task/install/ipmpls-northstar-traffic-updates-overview.html — The official doc archive says: &#x27;Juniper WANDL IP/MPLSView solution has reached end-of-support (EOS).&#x27; No successor product is named.</p>

<p>https://www.juniper.net/us/en/products/network-automation/paragon-planner.html — The Paragon Planner product URL now redirects to a generic hpe.com products page, so I could not use it to confirm an official successor relationship.</p>

<p>Caveats: The EOL milestone page is JavaScript-rendered, so I could not read the exact EOS dates.; The maintainer may prefer to add Paragon Planner as a separate new entry rather than treat it as a replacement.</p>

</details>

<h3>Unimus — update</h3>

```diff
--- a/README.md
+++ b/README.md
@@ -481,7 +481,7 @@
 - [Oxidized](https://github.com/ytti/oxidized) - Oxidized is a network device configuration backup tool. It's a RANCID replacement!
 - [RANCID](https://www.shrubbery.net/rancid) - RANCID monitors a router's (or more generally a device's) configuration, including software and hardware (cards, serial numbers, etc) and uses CVS (Concurrent Version System), Subversion or Git to maintain history of changes.
 - [Sweet](https://github.com/AppliedTrust/sweet) - Network device configuration backups and change alerts for the 21st century - inspired by RANCID!
-- [Unimus](https://unimus.net) - Configuration backup with an easy to use Web GUI. From nothing to backing-up 1000 routers in 15 minutes.
+- [Unimus](https://unimus.net) - Configuration backup, change management and network automation with an easy to use Web GUI.
 
 # IPAM
 - [bluecat](https://bluecatnetworks.com/adaptive-dns/bluecat-integrity/) - BlueCat provides network intelligence and insight into the relationship between devices, users and IP addresses that can be put into action to improve security and ensure reliable, always-on business connectivity.
```

<details>
<summary>Evidence and limitations</summary>

<p>Unimus is still a relevant vendor tool for config backup and network automation with a web GUI, available at unimus.net. However, the listed volatile claim &#x27;From nothing to backing-up 1000 routers in 15 minutes&#x27; no longer matches the official site. The features page now says &#x27;managing and automating a network of 1000 devices in 20 minutes&#x27;, and the product has grown to cover change management, compliance and config push automation. Recommend durable wording without counts.</p>

<p>https://unimus.net/features.html — The page contains the text &#x27;... managing and automating a network of 1000 devices in 20 minutes.&#x27; It lists Configuration Backup, Change Management (with REST API), Change Notifications, Configuration Auditing, Compliance, and Config Push Automation.</p>

<p>https://unimus.net/ — The homepage is titled &#x27;Unimus by NetCore j.s.a. | Network Automation, Configuration Backup &amp; Change Management&#x27;. It highlights a vendor-agnostic, web-based GUI and says deployment &#x27;requires only minutes&#x27;.</p>

<p>Caveats: I did not run the software, so the deployment-time claims are untested either way.</p>

</details>

<h3>bluecat — update</h3>

```diff
--- a/README.md
+++ b/README.md
@@ -484,7 +484,7 @@
 - [Unimus](https://unimus.net) - Configuration backup with an easy to use Web GUI. From nothing to backing-up 1000 routers in 15 minutes.
 
 # IPAM
-- [bluecat](https://bluecatnetworks.com/adaptive-dns/bluecat-integrity/) - BlueCat provides network intelligence and insight into the relationship between devices, users and IP addresses that can be put into action to improve security and ensure reliable, always-on business connectivity.
+- [bluecat](https://bluecatnetworks.com/products/integrity/) - BlueCat provides network intelligence and insight into the relationship between devices, users and IP addresses that can be put into action to improve security and ensure reliable, always-on business connectivity.
 - [Device42](https://www.device42.com) - Automatically maintain an up-to-date inventory of your physical, virtual, and cloud servers and containers, network components, software, services, applications, and their inter-relationships and inter-dependencies. Integrations, REST APIs and webhooks to automate your workflows with a modern CMDB as a single source of truth. Comes with powerful Data Center Infrastructure Management, IP Address Management and Application Mappings.  Mostly leverages SNMP or vendor provided APIs that are well adopted/documented.
 - [Infoblox](https://www.infoblox.com/) - Industry leader in DNS, DHCP, and IP address management, the category known as DDI.
 - [NetBox](https://github.com/netbox-community/netbox) - NetBox is an IP address management (IPAM) and data center infrastructure management (DCIM) tool.
```

<details>
<summary>Evidence and limitations</summary>

<p>The listed URL redirects to BlueCat&#x27;s canonical Integrity product page, https://bluecatnetworks.com/products/integrity/. The product is still an API-first DDI (DNS, DHCP, IPAM) platform that automates provisioning, so it fits the IPAM section. The existing description is generic marketing but not contradicted. The recommended correction is the canonical URL only.</p>

<p>https://bluecatnetworks.com/adaptive-dns/bluecat-integrity/ — Redirects (HTTP 200) to https://bluecatnetworks.com/products/integrity/, titled &#x27;Integrity – BlueCat Networks&#x27;.</p>

<p>https://bluecatnetworks.com/products/integrity/ — The page says: &#x27;An integrated DNS, DHCP, and IPAM (DDI) management platform, Integrity simplifies operations, automates provisioning...&#x27; It calls the product &#x27;Open API-first&#x27; with ServiceNow integration, and mentions real-time visibility.</p>

<p>Caveats: The maintainer may optionally rewrite the description to name Integrity as a DDI/IPAM platform. The current text is not factually false.</p>

</details>

<h3>UNetLab — update</h3>

```diff
--- a/README.md
+++ b/README.md
@@ -460,7 +460,7 @@
  - [Mininet](http://mininet.org/) - Mininet creates a realistic virtual network, running real kernel, switch and application code, on a single machine (VM, cloud or native), in seconds, with a single command.
  - [NetPilot](https://netpilot.io) - AI agent that designs, builds, and validates multi-vendor network labs from a plain-English prompt. Deploys 9+ real NOSes and growing (Cisco, Juniper, Arista, Nokia, Palo Alto, Fortinet, Aruba) on containerlab-based cloud sandboxes with real device CLIs.
  - [netlab](https://github.com/ipspace/netlab) - Brings infrastructure-as-code concepts to networking labs. You'll describe your high-level network topology and routing design in a YAML file, and the tools in this repository will create configs for VirtualBox/libvirt/containerlab, Ansible inventory, IPv4/v6 addressing, VLANs and VRFs, OSPF, EIGRP, IS-IS, BGP, BFD, MPLS, MPLS/VPN, VXLAN, EVPN and Segment Routing.
- - [UNetLab](https://www.routereflector.com/unetlab/) - Unified Networking Lab.
+ - [UNetLab](https://github.com/dainok/unetlab) - Unified Networking Lab.
  - [VRNetLab](https://github.com/plajjan/vrnetlab) - Run your favourite virtual routers in docker for convenient labbing, development and testing.
 
 # Network Simulators
```

<details>
<summary>Evidence and limitations</summary>

<p>The listed URL https://www.routereflector.com/unetlab/ no longer serves UNetLab content. It returns a JavaScript &#x27;Loading...&#x27; interstitial that redirects to a tokenized ww547.routereflector.com host (HTTP 401 &#x27;Forbidden&#x27;). The domain root www.routereflector.com 302-redirects to an unrelated site (surveymrs.com), which suggests the domain has lapsed or is parked. The author&#x27;s official source repository, github.com/dainok/unetlab, describes UNetLab (multi-hypervisor networking lab with IOU, Dynamips and QEMU nodes). It was archived in Aug 2026, but archival is not a removal reason for a historic emulator. Recommend moving the link to the canonical repo and keeping the short description.</p>

<p>https://www.routereflector.com/unetlab/ — Returns a JS redirect page titled &#x27;Loading...&#x27;. Following it lands on http://ww547.routereflector.com/?tkn=... with 401 Forbidden. No UNetLab content.</p>

<p>https://www.routereflector.com/ — Responds with 302 Location: http://surveymrs.com, a destination unrelated to UNetLab.</p>

<p>https://github.com/dainok/unetlab — The page reads &#x27;archived by the owner on Aug 5, 2026&#x27;. The README says &#x27;UNetLab is a new generation software for networking lab ... design labs using IOU, Dynamips and QEMU nodes&#x27;.</p>

<p>https://www.adainese.it/blog/2019/01/01/unified-networking-lab-unetlab-the-story/ — The author&#x27;s history post (HTTP 200 via curl) explains that EVE-NG was forked from UNetLab by others in 2017. The author is not part of the EVE-NG team, so EVE-NG is not an official successor.</p>

<p>Caveats: The routereflector.com redirect behavior could change, but the observed destination is unrelated to the project.; EVE-NG is a community fork rather than an author-designated successor, so replace was not proposed.</p>

<p>Source snapshot incomplete; excluded from the saved baseline.</p>

</details>

<h3>Cisco WAN Automation Engine — replace</h3>

```diff
--- a/README.md
+++ b/README.md
@@ -466,7 +466,7 @@
 # Network Simulators
 
  - [Batfish](https://github.com/batfish/batfish) - Batfish provides a model-based simulation for multi-vendor networks, that enables routing, forwarding, security, compliance, and what-if scenario analysis of a network (or proposed change to a network).
- - [Cisco WAN Automation Engine](https://www.cisco.com/c/en/us/products/routers/wae-planning/index.html) - Cisco WAE, formerly known as Cariden MATE, provides a multi-vendor network simulation that enables capacity planning and what-if scenario analysis for carrier networks.
+ - [Cisco Crosswork Planning](https://www.cisco.com/site/us/en/products/networking/software/crosswork-planning/index.html) - Cisco Crosswork Planning, the successor to Cisco WAE (formerly Cariden MATE), provides network modeling and simulation for capacity planning, failure and what-if scenario analysis.
  - [Forward Networks](https://forwardnetworks.com) - Forward Enterprise documents, searches, verifies, and predicts the behavior of your network by creating an always-accurate software copy of your entire network infrastructure for both on-prem and cloud.
  - [Juniper WANDL](https://www.juniper.net/us/en/products-services/sdn/wandl/) - Juniper WANDL provides traffic engineering
 models that enable capacity planning, network optimization and what-if scenario analysis for carrier networks.
```

<details>
<summary>Evidence and limitations</summary>

<p>Cisco has issued an End-of-Sale/End-of-Life announcement covering all Cisco WAN Automation Engine versions, including WAE 7.6 and MATE products. The last order date is November 15, 2026 and the last date of support is May 31, 2028. The notice names Cisco Crosswork Planning as the migration product, &#x27;our next-generation network planning and optimization platform ... that surpass[es] the sunsetting Cisco WAE&#x27;. Crosswork Planning provides network modeling, simulation, failure and what-if analysis, and capacity planning. The listed WAE page still loads via WebFetch (curl gets 403 from Akamai), so this is an officially documented successor, not a dead link.</p>

<p>https://www.cisco.com/c/en/us/products/collateral/routers/wan-automation-engine/wan-automation-engine-eol.html — The EOL notice gives End-of-Sale November 15, 2026 and Last Date of Support May 31, 2028. All WAE versions, including 7.6 and MATE, are affected. It recommends migrating to Cisco Crosswork Planning and links its datasheet.</p>

<p>https://www.cisco.com/c/en/us/products/routers/wae-planning/index.html — The page still describes WAE modeling, simulating and analyzing failures and what-if and capacity planning, and links to the EOL notices listing. It returns 403 to curl but was readable via WebFetch.</p>

<p>https://www.cisco.com/site/us/en/products/networking/software/crosswork-planning/index.html — The Crosswork Planning product page describes capacity planning, what-if scenarios and a simulation analysis tool.</p>

<p>https://www.cisco.com/c/en/us/products/cloud-systems-management/crosswork-network-automation/crosswork-planning-ds.html — From search excerpts: the datasheet describes discovery, analysis, simulation and optimization, modeling IGP, MPLS, RSVP-TE, Segment Routing, BGP and VPN, with failure what-if analysis.</p>

<p>Caveats: WAE remains supported until May 31, 2028, so the maintainer could keep the entry until then. Its end-of-sale is days away (Nov 15, 2026).; I did not confirm that Crosswork Planning is multi-vendor, so the proposed description omits that claim.; I read the datasheet details through search excerpts rather than a full page read.</p>

<p>Source snapshot incomplete; excluded from the saved baseline.</p>

</details>

<h3>NetMRI — update</h3>

```diff
--- a/README.md
+++ b/README.md
@@ -496,7 +496,7 @@
 # Configuration Management
 - [Jerikan](https://github.com/jerikan-network/cmdb) - Network wide CMDB combining single source of truth in YAML, configs in Jinja2 and deployment with Ansible.
 - [ManageEngine](https://www.manageengine.com/network-configuration-manager/) - Network Configuration Manager is a multi vendor network change, configuration and compliance management (NCCCM) solution for switches, routers, firewalls and other network devices.
-- [NetMRI](https://www.infoblox.com/products/netmri/) - Vendor Agnostic NCCM tool with with policy engine and multi-vendor device lifecycle/vulnerability management. (Infoblox product)
+- [NetMRI](https://www.infoblox.com/products/netmri/) - Vendor Agnostic NCCM tool with policy engine and multi-vendor device lifecycle/vulnerability management. (Infoblox product)
 - [Rconfig](https://www.rconfig.com/) - Free, open source network device configuration management tool, customizable to your needs!
 - [Solarwinds](https://www.solarwinds.com/network-configuration-manager) - Automated network configuration and compliance management.
 - [Unimus](https://unimus.net) - Network-wide configuration search and config diff over time in an easy to use web GUI.
```

<details>
<summary>Evidence and limitations</summary>

<p>The NetMRI product page is live. It supports every listed capability: multi-vendor management, policy and compliance enforcement, and lifecycle/vulnerability notices (security advisories and end-of-sale/support notices). The only correction is the duplicated word &#x27;with with&#x27; in the description.</p>

<p>https://www.infoblox.com/products/netmri/ — The page says: &#x27;Smartly manage your multi-vendor network with automation, visibility and continuous insight&#x27;; &#x27;Policy and compliance enforcement&#x27;; &#x27;out-of-the-box configuration policies&#x27;; &#x27;Advisories and end of sale/support notices impacting your devices&#x27;; network-wide change automation.</p>

<p>Caveats: This is a typo fix only. Relevance and identity are unchanged.</p>

</details>

<h3>Git Pocket Guide — update</h3>

```diff
--- a/README.md
+++ b/README.md
@@ -508,7 +508,7 @@
 - [Automate the Boring Stuff with Python](https://automatetheboringstuff.com/) - Automate the Boring Stuff with Python is an excellent introduction to programming concepts with a focus on Python. The concepts are made easier to learn by practicing them with hands on real world examples and projects.
 - [Cloud Native Data Center Networking](https://www.oreilly.com/library/view/cloud-native-data/9781492045595/) - If you want to study, build, or simply validate your thinking about modern cloud native data center networks, this is your book. Whether you’re pursuing a multitenant private cloud, a network for running machine learning, or an enterprise data center, author Dinesh Dutt takes you through the steps necessary to design a data center that’s affordable, high capacity, easy to manage, agile, and reliable.
 - [Effective DevOps](https://www.amazon.com/Effective-DevOps-Building-Collaboration-Affinity/dp/1491926309/) - Learn cultural and organizational best practices on how to make a good DevOps team
-- [Git Pocket Guide](http://chimera.labs.oreilly.com/books/1230000000561) - This pocket guide is the perfect on-the-job companion to Git, the distributed version control system. It provides a compact, readable introduction to Git for new users, as well as a reference to common commands and procedures for those of you with Git experience.
+- [Git Pocket Guide](https://www.oreilly.com/library/view/git-pocket-guide/9781449327507/) - This pocket guide is the perfect on-the-job companion to Git, the distributed version control system. It provides a compact, readable introduction to Git for new users, as well as a reference to common commands and procedures for those of you with Git experience.
 - [Infrastructure as Code](https://www.amazon.com/Infrastructure-Code-Managing-Servers-Cloud/dp/1491924357) - Learn the Infra as Code principles and design patterns (examples are for Compute not network though)
 - [Mastering Python Networking Second Edition (August 2018)](https://amzn.to/2PkMRiZ), [First Edition (June 2017 with more SDN-related topics)](https://amzn.to/2NBjlVM) - Become an expert in implementing advanced, network-related tasks with Python.
 - [Network Programmability and Automation](https://shop.oreilly.com/product/0636920042082.do) - Skills for the Next-Generation Network Engineer.
```

<details>
<summary>Evidence and limitations</summary>

<p>The listed chimera.labs.oreilly.com URL returns a 301 redirect to the generic O&#x27;Reilly homepage, so it no longer identifies the book. The book is still in O&#x27;Reilly&#x27;s library at a book-specific path. Updating the URL fixes the link; the description stays as is.</p>

<p>http://chimera.labs.oreilly.com/books/1230000000561 — curl -I: &#x27;HTTP/1.1 301 Moved Permanently&#x27;, &#x27;location: https://www.oreilly.com/&#x27;. It lands on the O&#x27;Reilly homepage (&#x27;O&#x27;Reilly Media - Technology and Business Training&#x27;), not a book page.</p>

<p>https://www.oreilly.com/library/view/git-pocket-guide/9781449327507/pr01.html — A search result shows &#x27;Preface - Git Pocket Guide [Book]&#x27; on O&#x27;Reilly at /library/view/git-pocket-guide/9781449327507/ (Richard E. Silverman, O&#x27;Reilly, 2013). This is the book-specific canonical path.</p>

<p>https://books.google.com/books/about/Git_Pocket_Guide.html?id=tPv2vX2czJoC — Bibliographic record for Git Pocket Guide: A Working Introduction, by Richard E. Silverman, O&#x27;Reilly, 2013.</p>

<p>Caveats: O&#x27;Reilly library pages return 403 to automated fetches. I confirmed the new URL from search-engine indexing of its subpages rather than loading it directly.; The book covers Git 1.8.2. It is still a valid introduction, but it is dated.</p>

</details>

<h3>Site Reliability Engineering and The Site Reliability Workbook — update</h3>

```diff
--- a/README.md
+++ b/README.md
@@ -515,7 +515,7 @@
 - [Network Programmability with YANG](https://www.oreilly.com/library/view/network-programmability-with/9780135180471/) - The Structure of Network Automation with YANG, NETCONF, RESTCONF, and gNMI.
 - [Network Automation at Scale](https://www.oreilly.com/webops-perf/free/network-automation-at-scale.csp) - An introduction and practical look at using Salt to automate your network at scale, in a free ebook from O'Reilly.
 - [Open Source Network Management](https://leanpub.com/opensourcenetworkmanagement/) - Step by step guide for getting started with Open Source Network Management tools such as Nautobot, Hashicorp Vault, Telegraf, and Prometheus.
-- [Site Reliability Engineering and The Site Reliability Workbook](https://landing.google.com/sre/book.html) - Learn concepts of automating and operating at scale from Google experts.
+- [Site Reliability Engineering and The Site Reliability Workbook](https://sre.google/books/) - Learn concepts of automating and operating at scale from Google experts.
 - [Seeking SRE: Conversations About Running Production Systems at Scale](https://www.amazon.com/Seeking-SRE-Conversations-Running-Production/dp/1491978864) - Learn from the best practices of SRE practitioners who are not working at Google.
 - [The DevOps Handbook](https://itrevolution.com/book/the-devops-handbook/) - Learn the concepts of Agile and DevOps principles.
 - [The Phoenix Project](https://itrevolution.com/book/the-phoenix-project/) - See the concepts of Agile and DevOps in this fiction story about a typical IT Org.
```

<details>
<summary>Evidence and limitations</summary>

<p>landing.google.com/sre/book.html redirects (2 hops) to the official canonical page https://sre.google/books/. That page still lists Site Reliability Engineering, its new 2nd Edition, and The Site Reliability Workbook, so the name and description still hold. The only change is updating the URL to the canonical one.</p>

<p>https://landing.google.com/sre/book.html — curl -L resolves to https://sre.google/books/ with HTTP 200 after 2 redirects.</p>

<p>https://sre.google/books/ — The Books page lists &#x27;Site Reliability Engineering, 2nd Edition&#x27;, &#x27;Building Secure &amp; Reliable Systems&#x27;, &#x27;The Site Reliability Workbook&#x27; and &#x27;Site Reliability Engineering&#x27;. It says the books teach the principles and practices Google uses to make large systems scalable, reliable and efficient.</p>

<p>Caveats: The 2nd Edition is new. The entry&#x27;s general wording still covers it, so no description change is needed.</p>

</details>

<h3>The DevOps Handbook — update</h3>

```diff
--- a/README.md
+++ b/README.md
@@ -517,7 +517,7 @@
 - [Open Source Network Management](https://leanpub.com/opensourcenetworkmanagement/) - Step by step guide for getting started with Open Source Network Management tools such as Nautobot, Hashicorp Vault, Telegraf, and Prometheus.
 - [Site Reliability Engineering and The Site Reliability Workbook](https://landing.google.com/sre/book.html) - Learn concepts of automating and operating at scale from Google experts.
 - [Seeking SRE: Conversations About Running Production Systems at Scale](https://www.amazon.com/Seeking-SRE-Conversations-Running-Production/dp/1491978864) - Learn from the best practices of SRE practitioners who are not working at Google.
-- [The DevOps Handbook](https://itrevolution.com/book/the-devops-handbook/) - Learn the concepts of Agile and DevOps principles.
+- [The DevOps Handbook](https://itrevolution.com/product/the-devops-handbook-second-edition/) - Learn the concepts of Agile and DevOps principles.
 - [The Phoenix Project](https://itrevolution.com/book/the-phoenix-project/) - See the concepts of Agile and DevOps in this fiction story about a typical IT Org.
 - [The Unicorn Project](https://itrevolution.com/the-unicorn-project/) - See the concepts of Agile and DevOps following a Developer viewpoint.
 
```

<details>
<summary>Evidence and limitations</summary>

<p>The listed URL redirects (1 hop) to the publisher&#x27;s canonical product page for the second edition. The book is still published, and the general DevOps-principles description still holds. The only change is updating the URL to the canonical one.</p>

<p>https://itrevolution.com/book/the-devops-handbook/ — Resolves to https://itrevolution.com/product/the-devops-handbook-second-edition/ (HTTP 200).</p>

<p>https://itrevolution.com/product/the-devops-handbook-second-edition/ — Meta description: &#x27;This award-winning and bestselling business handbook for digital transformation is now fully updated and expanded with the latest research and new case studies&#x27;.</p>

<p>Caveats: The old URL still redirects, so the update is optional.</p>

</details>

<h3>The Phoenix Project — update</h3>

```diff
--- a/README.md
+++ b/README.md
@@ -518,7 +518,7 @@
 - [Site Reliability Engineering and The Site Reliability Workbook](https://landing.google.com/sre/book.html) - Learn concepts of automating and operating at scale from Google experts.
 - [Seeking SRE: Conversations About Running Production Systems at Scale](https://www.amazon.com/Seeking-SRE-Conversations-Running-Production/dp/1491978864) - Learn from the best practices of SRE practitioners who are not working at Google.
 - [The DevOps Handbook](https://itrevolution.com/book/the-devops-handbook/) - Learn the concepts of Agile and DevOps principles.
-- [The Phoenix Project](https://itrevolution.com/book/the-phoenix-project/) - See the concepts of Agile and DevOps in this fiction story about a typical IT Org.
+- [The Phoenix Project](https://itrevolution.com/product/the-phoenix-project/) - See the concepts of Agile and DevOps in this fiction story about a typical IT Org.
 - [The Unicorn Project](https://itrevolution.com/the-unicorn-project/) - See the concepts of Agile and DevOps following a Developer viewpoint.
 
 # Vendor Agnostic Products
```

<details>
<summary>Evidence and limitations</summary>

<p>The listed URL redirects to the canonical IT Revolution product page. The page confirms the book is a DevOps novel about an IT manager, which matches the description. Only the URL changes.</p>

<p>https://itrevolution.com/book/the-phoenix-project/ — Resolves to https://itrevolution.com/product/the-phoenix-project/ (HTTP 200).</p>

<p>https://itrevolution.com/product/the-phoenix-project/ — Meta description: &#x27;The bestselling novel that introduced the world to DevOps and the Three Ways — an IT manager with 90 days to save his company. By Gene Kim, Behr &amp; Spafford.&#x27;</p>

<p>Caveats: The old URL still redirects, so the update is optional.</p>

</details>

<h3>The Unicorn Project — update</h3>

```diff
--- a/README.md
+++ b/README.md
@@ -519,7 +519,7 @@
 - [Seeking SRE: Conversations About Running Production Systems at Scale](https://www.amazon.com/Seeking-SRE-Conversations-Running-Production/dp/1491978864) - Learn from the best practices of SRE practitioners who are not working at Google.
 - [The DevOps Handbook](https://itrevolution.com/book/the-devops-handbook/) - Learn the concepts of Agile and DevOps principles.
 - [The Phoenix Project](https://itrevolution.com/book/the-phoenix-project/) - See the concepts of Agile and DevOps in this fiction story about a typical IT Org.
-- [The Unicorn Project](https://itrevolution.com/the-unicorn-project/) - See the concepts of Agile and DevOps following a Developer viewpoint.
+- [The Unicorn Project](https://itrevolution.com/product/the-unicorn-project/) - See the concepts of Agile and DevOps following a Developer viewpoint.
 
 # Vendor Agnostic Products
 - [Anuta Networks ATOM](https://www.anutanetworks.com/anuta-atom-overview/) - Monitoring & Closed-Loop Automation for Multi-Vendor Networks.
```

<details>
<summary>Evidence and limitations</summary>

<p>The listed URL redirects to the canonical IT Revolution product page. The page describes the book as the follow-up to The Phoenix Project that presents the Five Ideals of Software Development, which fits the &#x27;Developer viewpoint&#x27; description. Only the URL changes.</p>

<p>https://itrevolution.com/the-unicorn-project/ — Resolves to https://itrevolution.com/product/the-unicorn-project/ (HTTP 200).</p>

<p>https://itrevolution.com/product/the-unicorn-project/ — Meta description: &#x27;The highly anticipated follow-up to the bestselling title The Phoenix Project, this book unveils the Five Ideals of Software Development.&#x27;</p>

<p>Caveats: The old URL still redirects, so the update is optional.</p>

</details>

<h3>Intentionet — remove</h3>

<p>0 proposed change(s); 1 held for unresolved questions.</p>

<details>
<summary>Evidence and limitations</summary>

<p>Intentionet&#x27;s own domain now redirects to batfish.org. That page says Batfish &#x27;was later enhanced and maintained by Intentionet. Since the Intentionet team joined AWS, it has been an AWS-managed open source project.&#x27; The vendor no longer runs a product site, and I found no current official offering of the hosted/on-premise &#x27;Intentionet Sage&#x27; product the entry describes. Batfish itself is already listed elsewhere in the catalog (its own section and the tools lists), so redirecting this vendor entry to Batfish would duplicate it.</p>

<p>https://www.intentionet.com/ — Redirects to https://intentionet.com/, which returns only &#x27;Redirecting to https://batfish.org&#x27;.</p>

<p>https://batfish.org/ — &#x27;Batfish was originally developed by researchers at Microsoft Research, UCLA, and USC. It was later enhanced and maintained by Intentionet. Since the Intentionet team joined AWS, it has been an AWS-managed open source project under the same license (Apache 2.0).&#x27;</p>

<p>https://www.geekwire.com/2022/amazon-web-services-inks-licensing-deal-with-seattle-startup-intentionet-developers-of-batfish/ — The search snippet says AWS signed a licensing deal with Intentionet in Sept 2022 and the team joined Amazon. Only the snippet was seen; I did not read the article directly.</p>

<p>Caveats: I found no explicit official end-of-sale notice for Intentionet Sage. The evidence is the vendor domain redirecting away and the team joining AWS.; Batfish remains listed separately in the catalog (README lines ~274, 402, 468).</p>

</details>

<h3>NetMRI — update</h3>

```diff
--- a/README.md
+++ b/README.md
@@ -529,7 +529,7 @@
 - [Glue](http://gluenetworks.com/about-us-the-glue-team/) - With Gluware, the Glue Networks vision and team are continuing to trail-blaze at the forefront of the networking industry with multi-vendor orchestration solutions for Data Center, WAN and LAN networks.
 - [Intentionet](https://www.intentionet.com/) - Intentionet provides a hosted or on-premise network validation software solution based on [Batfish](http://www.batfish.org). Intentionet Sage's model-based network simulation enables pre-commit validation for all network changes, ensuring only correct changes are pushed to the network, thereby reducing outages and breaches while improving network agility.
 - [IP Fabric](https://ipfabric.io/) - Network assurance tool with vendor agnostic network discovery, inventory, modelling and mapping of on-prem and cloud networks.  Snapshots create a point-in-time view to verify that network behaves as intended after changes. GUI supports your network documentation with accurate, live network representation, and API used to keep all your SoT, automation tooling and monitoring up to date.
-- [NetMRI](https://www.infoblox.com/products/netmri/) - Vendor Agnostic NCCM tool with with policy engine and multi-vendor device lifecycle/vulnerability management. (Infoblox product)
+- [NetMRI](https://www.infoblox.com/products/netmri/) - Vendor Agnostic NCCM tool with policy engine and multi-vendor device lifecycle/vulnerability management. (Infoblox product)
 - [NetYCE](https://netyce.com/) NetYCE lets you be in control of any and all of your networks, using its unique Design Driven Networking approach. Not stopping at network devices, but orchestrate end-to-end including firewalls, DDI (DNS, DHCP, IPAM) and other 3rd party tooling. Deploy your networks as Designed.
 - [PacketFront](https://pfsw.com/) - PacketFront BECS and BBE is a vendor-agnostic network, service and resource orchestration system for residential, enterprise and data center networks.
 - [SuzieQ Enterprise Edition](https://stardustsystems.net) - The enterprise edition of the [suzieq](#suzieq) open source project.
```

<details>
<summary>Evidence and limitations</summary>

<p>The Infoblox NetMRI page is live. It confirms a multi-vendor network change and configuration management (NCCM) product with policy enforcement and compliance auditing, plus NetMRI Advisor for PSIRTs, advisories and end-of-sale/support notices. That covers the entry&#x27;s policy engine and lifecycle/vulnerability claims, so fit and facts hold. The entry has a duplicated word, &#x27;with with&#x27;, which this update fixes.</p>

<p>https://www.infoblox.com/products/netmri/ — &#x27;It&#x27;s a network change and configuration management solution that automates routine workflows such as device provisioning and security operations.&#x27; &#x27;Smartly manage your multi-vendor network.&#x27; &#x27;Automatically enforce and continually audit network infrastructure configurations ... across multi-vendor equipment.&#x27; &#x27;Leverage NetMRI Advisor for continuous updates and monitoring for PSIRTs, Advisories and end of sale/support notices&#x27;.</p>

<p>Caveats: The change is only a typo fix. Keeping the entry as-is would also be reasonable.</p>

</details>

<h3>Apstra — update</h3>

<p>0 proposed change(s); 1 held for unresolved questions.</p>

<details>
<summary>Evidence and limitations</summary>

<p>apstra.com times out on HTTP and has a mismatched certificate on HTTPS. Juniper bought Apstra, and HPE bought Juniper. Juniper&#x27;s Apstra product page and docs URLs now 301-redirect to HPE (hpe.com/us/en/products/networking/data-center-director.html and networkingdocs.hpe.com/.../apstra/), where the product is called &#x27;Apstra Data Center Director&#x27;. The &#x27;Apstra Operating System (AOS)&#x27; name in the entry is outdated. The product is still intent-based data center network automation, so it still fits.</p>

<p>https://www.apstra.com/products/ — Connection timed out. https://apstra.com/ fails with an SSL certificate name mismatch.</p>

<p>https://www.juniper.net/us/en/products/network-automation/apstra-data-center-director.html — Returns 301 Moved Permanently to https://www.hpe.com/us/en/products/networking/data-center-director.html.</p>

<p>https://networkingdocs.hpe.com/documentation/product/us/en/apstra/ — Official docs landing page (redirected from juniper.net/documentation/product/us/en/apstra/) is titled &#x27;Apstra Data Center Director&#x27;.</p>

<p>Blocking questions: I could not read the destination HPE product page directly (timeouts), so its exact wording and its multivendor claim are confirmed only through search snippets and the docs landing page.</p>

<p>Caveats: HPE uses several names: &#x27;HPE Networking Apstra Data Center Director&#x27;, &#x27;HPE Networking Data Center Director&#x27; and &#x27;Apstra Data Center Director&#x27;. The proposed name is the shortest common form.; The HPE product page timed out for both WebFetch and curl. Its contents come from search snippets (intent-based networking, multivendor fabric management).</p>

<p>Source snapshot incomplete; excluded from the saved baseline.</p>

</details>

<h3>Cisco NSO — update</h3>

```diff
--- a/README.md
+++ b/README.md
@@ -524,7 +524,7 @@
 # Vendor Agnostic Products
 - [Anuta Networks ATOM](https://www.anutanetworks.com/anuta-atom-overview/) - Monitoring & Closed-Loop Automation for Multi-Vendor Networks.
 - [Apstra](https://www.apstra.com/products/) - The Apstra Operating System (AOS) is a vendor-agnostic distributed operating system for the data center network that enables business agility, dramatically scales operational efficiency, and reduces downtime.
-- [Cisco NSO](https://cisco.com/go/nso) - NSO (former Tail-f NCS) is a multi-vendor automation and orchestration platform for physical and virtual networks for over 80+ vendors. NSO provides YANG-based programmability through a wide variety of interfaces including CLI, RESTCONF, NETCONF, Java, Python and web UI.
+- [Cisco NSO](https://cisco.com/go/nso) - NSO (Cisco Crosswork Network Services Orchestrator, formerly Tail-f NCS) is a multi-vendor automation and orchestration platform for physical and virtual networks. NSO provides YANG-based programmability through a wide variety of interfaces including CLI, RESTCONF, NETCONF, JSON-RPC, Java, Python and web UI.
  - [Forward Networks](https://forwardnetworks.com) - Forward Enterprise documents, searches, verifies, and predicts the behavior of your network by creating an always-accurate software copy of your entire network infrastructure for both on-prem and cloud.
 - [Glue](http://gluenetworks.com/about-us-the-glue-team/) - With Gluware, the Glue Networks vision and team are continuing to trail-blaze at the forefront of the networking industry with multi-vendor orchestration solutions for Data Center, WAN and LAN networks.
 - [Intentionet](https://www.intentionet.com/) - Intentionet provides a hosted or on-premise network validation software solution based on [Batfish](http://www.batfish.org). Intentionet Sage's model-based network simulation enables pre-commit validation for all network changes, ensuring only correct changes are pushed to the network, thereby reducing outages and breaches while improving network agility.
```

<details>
<summary>Evidence and limitations</summary>

<p>cisco.com/go/nso returns HTTP 403 to automated clients (bot blocking, not a dead link). The official NSO docs confirm the rest of the entry: Tail-f heritage (&#x27;enabled by Tail-f&#x27;, &#x27;ncs&#x27; naming), YANG-based multi-vendor device management, and northbound CLI, web UI, RESTCONF, NETCONF, JSON-RPC, and Java/Python/Erlang bindings. The &#x27;80+ vendors&#x27; count isn&#x27;t stated in the current docs. Cisco now cites support for 1,000+ third-party device types via NEDs (search snippet), so the volatile count should be dropped. The product is now formally named Cisco Crosswork Network Services Orchestrator.</p>

<p>https://nso-docs.cisco.com/nso-basics/nso-at-a-glance — &#x27;NSO uses YANG as the overall modeling language to manage devices and services.&#x27; &#x27;human interfaces like web UI and a CLI, programmable interfaces including RESTCONF, NETCONF, JSON-RPC, and language bindings including Java, Python, and Erlang.&#x27; It calls the product &#x27;Cisco Crosswork Network Services Orchestrator (NSO) enabled by Tail-f&#x27; and gives no vendor count.</p>

<p>https://developer.cisco.com/docs/nso/ — Official DevNet NSO documentation page is live (HTTP 200).</p>

<p>https://cisco.com/go/nso — Redirects to www.cisco.com/go/nso, which returns HTTP 403 to curl. This looks like Cisco&#x27;s bot filtering.</p>

<p>Caveats: The 1,000+ third-party device types figure comes from a search snippet of the Cisco NED datasheet. I did not read it directly, so the proposed wording avoids any count.; I did not change the URL. cisco.com/go/nso is Cisco&#x27;s own short link and likely works in browsers.</p>

<p>Source snapshot incomplete; excluded from the saved baseline.</p>

</details>

<h3>Glue — update</h3>

```diff
--- a/README.md
+++ b/README.md
@@ -526,7 +526,7 @@
 - [Apstra](https://www.apstra.com/products/) - The Apstra Operating System (AOS) is a vendor-agnostic distributed operating system for the data center network that enables business agility, dramatically scales operational efficiency, and reduces downtime.
 - [Cisco NSO](https://cisco.com/go/nso) - NSO (former Tail-f NCS) is a multi-vendor automation and orchestration platform for physical and virtual networks for over 80+ vendors. NSO provides YANG-based programmability through a wide variety of interfaces including CLI, RESTCONF, NETCONF, Java, Python and web UI.
  - [Forward Networks](https://forwardnetworks.com) - Forward Enterprise documents, searches, verifies, and predicts the behavior of your network by creating an always-accurate software copy of your entire network infrastructure for both on-prem and cloud.
-- [Glue](http://gluenetworks.com/about-us-the-glue-team/) - With Gluware, the Glue Networks vision and team are continuing to trail-blaze at the forefront of the networking industry with multi-vendor orchestration solutions for Data Center, WAN and LAN networks.
+- [Gluware](https://gluware.com/) - Gluware (formerly Glue Networks) provides an intelligent, intent-based network automation platform for multi-vendor configuration management, audit/compliance, OS upgrades and workflow orchestration across data center, WAN and LAN networks.
 - [Intentionet](https://www.intentionet.com/) - Intentionet provides a hosted or on-premise network validation software solution based on [Batfish](http://www.batfish.org). Intentionet Sage's model-based network simulation enables pre-commit validation for all network changes, ensuring only correct changes are pushed to the network, thereby reducing outages and breaches while improving network agility.
 - [IP Fabric](https://ipfabric.io/) - Network assurance tool with vendor agnostic network discovery, inventory, modelling and mapping of on-prem and cloud networks.  Snapshots create a point-in-time view to verify that network behaves as intended after changes. GUI supports your network documentation with accurate, live network representation, and API used to keep all your SoT, automation tooling and monitoring up to date.
 - [NetMRI](https://www.infoblox.com/products/netmri/) - Vendor Agnostic NCCM tool with with policy engine and multi-vendor device lifecycle/vulnerability management. (Infoblox product)
```

<details>
<summary>Evidence and limitations</summary>

<p>gluenetworks.com returns HTTP 502 / proxy errors, and the listed &#x27;about us&#x27; page can&#x27;t be reached. The company renamed itself from Glue Networks to Gluware, and its official company page says the founders started &#x27;initially bootstrapping the company as Glue Networks&#x27;. Gluware is live at gluware.com and offers a multi-vendor network automation platform (config drift/audit, OS manager, workflows, multi-vendor/data center/brownfield solutions). This is a confirmed rename of the same company, not a competitor.</p>

<p>http://gluenetworks.com/about-us-the-glue-team/ — HTTP 502. https://www.gluenetworks.com/ also fails (CONNECT 502).</p>

<p>https://gluware.com/company/ — Jeff Gray&#x27;s bio: he and Olivier Huynh Van &#x27;created the foundation for Gluware ... initially bootstrapping the company as Glue Networks.&#x27; The page describes &#x27;intent-based network automation&#x27; with solutions for Brownfield, Greenfield, Data Center and Multi-Vendor Networks.</p>

<p>https://gluware.com/ — &#x27;Gluware Intelligent Network Automation for the Agentic Era&#x27;. Apps include Config Drift and Audit, Device Manager, OS Manager, Workflows, Network RPA, GluAPI and an Ansible Certified Collection.</p>

<p>Caveats: Gluware&#x27;s homepage also promotes AI and agentic features (Gluware.ai, Titan). The description doesn&#x27;t need to list them.</p>

<p>Source snapshot incomplete; excluded from the saved baseline.</p>

</details>

<h3>Cisco DNA Center — update</h3>

```diff
--- a/README.md
+++ b/README.md
@@ -537,7 +537,7 @@
 # Network Vendor Products
 
 - [Arista CloudVision](https://www.arista.com/en/products/eos/eos-cloudvision) - CloudVision is Arista’s modern, multi-domain management platform that leverages cloud networking principles to deliver a simplified NetOps experience.
-- [Cisco DNA Center](https://developer.cisco.com/dnacenter/) - Cisco DNA Center automates campus networks for faster workflows, faster troubleshooting through more visibility, and policy-driven security (inc. [SDA](https://www.cisco.com/c/en/us/solutions/enterprise-networks/software-defined-access/index.html)).
+- [Cisco Catalyst Center](https://developer.cisco.com/catalyst-center/) - Cisco Catalyst Center (formerly DNA Center) automates campus networks for faster workflows, faster troubleshooting through more visibility, and policy-driven security (inc. [SDA](https://www.cisco.com/c/en/us/solutions/enterprise-networks/software-defined-access/index.html)).
 - [Cisco Meraki](https://meraki.cisco.com/) - Cisco Meraki is the leader in cloud controlled WiFi, routing, and security. Secure and scalable, Cisco Meraki enterprise networks simply work.
 - [Cisco Viptela](http://viptela.com/) - Viptela provides Software-Defined Wide Area Network (SD-WAN) technology that allows global companies to build cost-effective WANs.
 - [Cumulus Networks NetQ](https://cumulusnetworks.com/products/netq/) - Cumulus NetQ is a highly-scalable, modern network operations tool set that provides visibility into your overlay and underlay networks in real-time. NetQ delivers actionable insights and operational intelligence about the health of your data center — from the container, virtual machine, or host, all the way to the switch and port, enabling a NetDevOps approach.
```

<details>
<summary>Evidence and limitations</summary>

<p>Cisco renamed DNA Center to Catalyst Center (Cisco DevNet blog). The listed developer URL now 301-redirects to https://developer.cisco.com/catalyst-center/. That page describes Catalyst Center as an extensible platform with Intent APIs, integration flows, event notifications and policy abstraction, so the product still fits network automation. The SDA link returned HTTP 403 to curl (Cisco bot filtering), so I left it unchanged.</p>

<p>https://developer.cisco.com/dnacenter/ — 301 to /catalyst-center/ (HTTP 200).</p>

<p>https://developer.cisco.com/catalyst-center/ — &#x27;Cisco Catalyst Center provides an extensible platform ... through Intent APIs, integration flows, and event notifications.&#x27; Features include Policy Abstraction, ITSM integration flows, and Assurance and SWIM event notifications.</p>

<p>https://blogs.cisco.com/developer/cisco-dna-center-has-a-new-name-and-new-features — &#x27;Cisco DNA Center is not only getting a name change to Cisco Catalyst Center, it also offers lots of new features&#x27;. It notes that older API versions keep the DNA Center name.</p>

<p>Caveats: The SDA URL on cisco.com returned 403 to automated clients. I could not confirm its current content.; Catalyst Center may be folded into Cisco&#x27;s newer unified cloud-management branding later. That is not confirmed officially.</p>

<p>Source snapshot incomplete; excluded from the saved baseline.</p>

</details>

<h3>Cumulus Networks NetQ — update</h3>

```diff
--- a/README.md
+++ b/README.md
@@ -540,7 +540,7 @@
 - [Cisco DNA Center](https://developer.cisco.com/dnacenter/) - Cisco DNA Center automates campus networks for faster workflows, faster troubleshooting through more visibility, and policy-driven security (inc. [SDA](https://www.cisco.com/c/en/us/solutions/enterprise-networks/software-defined-access/index.html)).
 - [Cisco Meraki](https://meraki.cisco.com/) - Cisco Meraki is the leader in cloud controlled WiFi, routing, and security. Secure and scalable, Cisco Meraki enterprise networks simply work.
 - [Cisco Viptela](http://viptela.com/) - Viptela provides Software-Defined Wide Area Network (SD-WAN) technology that allows global companies to build cost-effective WANs.
-- [Cumulus Networks NetQ](https://cumulusnetworks.com/products/netq/) - Cumulus NetQ is a highly-scalable, modern network operations tool set that provides visibility into your overlay and underlay networks in real-time. NetQ delivers actionable insights and operational intelligence about the health of your data center — from the container, virtual machine, or host, all the way to the switch and port, enabling a NetDevOps approach.
+- [NVIDIA NetQ](https://www.nvidia.com/en-us/networking/ethernet-switching/netq/) - NVIDIA NetQ (formerly Cumulus NetQ) is a scalable network operations toolset that uses switch and host agents and streaming telemetry to provide real-time visibility, troubleshooting and validation of NVIDIA Cumulus and NVLink fabrics, enabling a NetDevOps approach.
 - [Oracle Talari](https://www.oracle.com/industries/communications/enterprise-communications/products/talari-platforms.html) - Talari Networks SD-WAN technology.
 
 # Podcasts
```

<details>
<summary>Evidence and limitations</summary>

<p>The product is still relevant, but its identity has changed. The old cumulusnetworks.com URL 301-redirects to NVIDIA&#x27;s NetQ page, and the vendor now calls the product &quot;NVIDIA NetQ&quot; (&quot;Cumulus NetQ&quot; survives only in the page title and docs path). NVIDIA describes it as a highly scalable network operations toolset that uses switch and host agents and telemetry for visibility, troubleshooting, correlation and validation. That still fits network automation (validation, telemetry, CI/CD-style operations). The listed claim of visibility &quot;from the container, virtual machine&quot; is no longer supported by current docs: the container-monitoring page exists in the NetQ 4.10 guide but returns 404 in 4.15 and 5.0 through 5.3. I recommend a rename, the canonical URL, and a description that leaves out the container/VM claim.</p>

<p>https://cumulusnetworks.com/products/netq/ — Redirects (1 hop) to https://www.nvidia.com/en-us/networking/ethernet-switching/netq/ with HTTP 200.</p>

<p>https://www.nvidia.com/en-us/networking/ethernet-switching/netq/ — Page says: &#x27;NVIDIA NetQ™ is a highly scalable network operations toolset that provides visibility, troubleshooting, correlation, and validation of your NVIDIA NVLink™ Switches and NVIDIA® Cumulus® fabrics in real time.&#x27; It also says &#x27;NetQ uses agents on the switches and hosts to collect telemetry data&#x27; and mentions &#x27;full continuous integration and continuous deployment (CI/CD) functionality&#x27; and &#x27;Preventive Validation&#x27;.</p>

<p>https://docs.nvidia.com/networking-ethernet-software/cumulus-netq/ — Current docs title: &#x27;NVIDIA NetQ 5.3 User Guide | Cumulus NetQ 5.3&#x27;.</p>

<p>https://docs.nvidia.com/networking-ethernet-software/cumulus-netq-410/Manage-Inventory/Monitor-Container-Environment/ — Kubernetes/container monitoring page exists in the NetQ 4.10 guide (HTTP 200). The same path returns 404 for 4.15, 5.0, 5.1, 5.2 and 5.3.</p>

<p>Caveats: A missing docs page is strong but not conclusive evidence that container monitoring was removed. I found no release note that explicitly removes it.; I did not run NetQ.</p>

</details>

<h3>Packet Pushers Full Stack — update</h3>

```diff
--- a/README.md
+++ b/README.md
@@ -548,7 +548,7 @@
 ## Podcasts Feeds
 
 - [Network to Code](https://networkcollective.com/category/episodes/network-to-code/) - Network to Code automation podcast on the Network Collective feed.
-- [Packet Pushers Full Stack](https://packetpushers.net/series/full-stack-journey/) - The Journey To Full Stack.
+- [Packet Pushers Full Stack](https://packetpushers.net/podcast/full-stack-journey/) - The Journey To Full Stack.
 - [Software Gone Wild](https://www.ipspace.net/Podcast/Software_Gone_Wild) - Software Gone Wild is focusing on architectures, solutions and technologies that real networking engineers use in production networks.
 
 ## Podcasts Episodes
```

<details>
<summary>Evidence and limitations</summary>

<p>The series page exists and 301-redirects to a new canonical URL. The page states Full Stack Journey &#x27;tells personal stories about the ongoing quest to become a full stack engineer&#x27; and that the series has ended (&#x27;The Final Journey Of Full Stack Journey&#x27;, more than 80 episodes over five years). The episodes include automation and DevOps topics (e.g. FSJ 020 with Jason Edelman on network automation, FSJ 079 on GitOps). A historic podcast can remain relevant. The description is still accurate, so only the URL needs updating.</p>

<p>https://packetpushers.net/series/full-stack-journey/ — 301 redirect to https://packetpushers.net/podcast/full-stack-journey/ (HTTP 200). rel=canonical is that URL.</p>

<p>https://packetpushers.net/podcast/full-stack-journey/ — Says &#x27;Full Stack Journey tells personal stories about the ongoing quest to become a full stack engineer...&#x27;. Latest item: &#x27;The Final Journey Of Full Stack Journey... After five years and more than 80 episodes... this is the final episode of the series.&#x27;</p>

<p>https://packetpushers.net/podcasts/full-stack-journey/full-stack-journey-020-jason-edelman-network-automation/ — Packet Pushers&#x27; podcast sitemap lists this episode URL, showing network-automation content within the series.</p>

<p>Caveats: The series is finished, so it is an archive rather than an active feed. That alone is not grounds for removal.</p>

</details>

<h3>Packet Pushers Day Two Cloud 043 — update</h3>

```diff
--- a/README.md
+++ b/README.md
@@ -556,7 +556,7 @@
 - [Network Collective EPISODE 10](https://thenetworkcollective.com/2017/08/ep10-grassroots-automation/) - GRASSROOTS AUTOMATION.
 - [Network Collective Infrastructure as Code 101](https://networkcollective.com/2019/09/infrastructure-as-code/) Introduction to Infrastructure as Code with Damien Garros and Ken Celenza.
 - [Packet Pushers Datanauts 80](https://packetpushers.net/podcast/podcasts/datanauts-080-network-automation-telemetry/) - The Current State Of Network Automation & Telemetry.
-- [Packet Pushers Day Two Cloud 043](https://packetpushers.net/podcast/day-two-cloud-043-git-for-ops-people/) - Git For Ops People with Damien Garros.
+- [Packet Pushers Day Two Cloud 043](https://packetpushers.net/podcasts/day-two-devops/d2c043-git-for-ops-people/) - Git For Ops People with Damien Garros.
 - [Packet Pushers Heavy Networking #445](https://packetpushers.net/podcast/heavy-networking-445-an-introduction-to-the-nornir-automation-framework/) - David Barroso, Kirk Byers, and Dmitri Figol on Nornir.
 - [Packet Pushers Heavy Networking #498](https://packetpushers.net/podcast/heavy-networking-498-creating-a-single-source-of-truth-for-network-automation/) - Creating A Single Source Of Truth For Network Automation with Tim Schreyack.
 - [Packet Pushers PQ Show 81](https://packetpushers.net/podcast/podcasts/pq-show-81-network-testing-todd/) - Network Testing With ToDD.
```

<details>
<summary>Evidence and limitations</summary>

<p>The episode exists. The old URL 301-redirects to a new canonical URL under Day Two DevOps, and the page confirms the topic (Git for operations people) and guest (Damien Garros of Network To Code). The description is accurate, so only the URL needs updating.</p>

<p>https://packetpushers.net/podcast/day-two-cloud-043-git-for-ops-people/ — Redirects to https://packetpushers.net/podcasts/day-two-devops/D2C043-git-for-ops-people/ (HTTP 200). Its rel=canonical and the podcast sitemap both give the lowercase https://packetpushers.net/podcasts/day-two-devops/d2c043-git-for-ops-people/.</p>

<p>https://packetpushers.net/podcasts/day-two-devops/d2c043-git-for-ops-people/ — Title &#x27;Day Two Cloud 043: Git For Ops People&#x27;. Meta description: &#x27;...Our guest is Damien Garros, Managing Director at Network To Code.&#x27;</p>

</details>

<h3>Packet Pushers Heavy Networking #445 — update</h3>

```diff
--- a/README.md
+++ b/README.md
@@ -557,7 +557,7 @@
 - [Network Collective Infrastructure as Code 101](https://networkcollective.com/2019/09/infrastructure-as-code/) Introduction to Infrastructure as Code with Damien Garros and Ken Celenza.
 - [Packet Pushers Datanauts 80](https://packetpushers.net/podcast/podcasts/datanauts-080-network-automation-telemetry/) - The Current State Of Network Automation & Telemetry.
 - [Packet Pushers Day Two Cloud 043](https://packetpushers.net/podcast/day-two-cloud-043-git-for-ops-people/) - Git For Ops People with Damien Garros.
-- [Packet Pushers Heavy Networking #445](https://packetpushers.net/podcast/heavy-networking-445-an-introduction-to-the-nornir-automation-framework/) - David Barroso, Kirk Byers, and Dmitri Figol on Nornir.
+- [Packet Pushers Heavy Networking #445](https://packetpushers.net/podcasts/heavy-networking/hn445-an-introduction-to-the-nornir-automation-framework/) - David Barroso, Kirk Byers, and Dmitry Figol on Nornir.
 - [Packet Pushers Heavy Networking #498](https://packetpushers.net/podcast/heavy-networking-498-creating-a-single-source-of-truth-for-network-automation/) - Creating A Single Source Of Truth For Network Automation with Tim Schreyack.
 - [Packet Pushers PQ Show 81](https://packetpushers.net/podcast/podcasts/pq-show-81-network-testing-todd/) - Network Testing With ToDD.
 - [Packet Pushers PQ Show 99](https://packetpushers.net/podcast/podcasts/pq-show-99-netmiko-napalm-network-automation/) - Netmiko & NAPALM For Network Automation.
```

<details>
<summary>Evidence and limitations</summary>

<p>The episode exists. The old URL redirects to a new canonical URL, and the page confirms the guests David Barroso, Kirk Byers and Dmitry Figol discussing Nornir. The description spells the name &#x27;Dmitri&#x27;, but the page uses &#x27;Dmitry&#x27;. That spelling fix is minor and optional, so I&#x27;ve preserved the description wording except for the spelling.</p>

<p>https://packetpushers.net/podcast/heavy-networking-445-an-introduction-to-the-nornir-automation-framework/ — Redirects to /podcasts/heavy-networking/HN445-.... rel=canonical and the sitemap give https://packetpushers.net/podcasts/heavy-networking/hn445-an-introduction-to-the-nornir-automation-framework/.</p>

<p>https://packetpushers.net/podcasts/heavy-networking/hn445-an-introduction-to-the-nornir-automation-framework/ — Title &#x27;Heavy Networking 445: An Introduction To The Nornir Automation Framework&#x27;. Page text: &#x27;Our guests today are David Barroso... Kirk Byers... and Dmitry Figol... All three guests help maintain Nornir.&#x27;</p>

<p>Caveats: The guest-name spelling change (Dmitri → Dmitry) follows the episode page. Maintainers may skip it.</p>

</details>

<h3>Packet Pushers Heavy Networking #498 — update</h3>

```diff
--- a/README.md
+++ b/README.md
@@ -558,7 +558,7 @@
 - [Packet Pushers Datanauts 80](https://packetpushers.net/podcast/podcasts/datanauts-080-network-automation-telemetry/) - The Current State Of Network Automation & Telemetry.
 - [Packet Pushers Day Two Cloud 043](https://packetpushers.net/podcast/day-two-cloud-043-git-for-ops-people/) - Git For Ops People with Damien Garros.
 - [Packet Pushers Heavy Networking #445](https://packetpushers.net/podcast/heavy-networking-445-an-introduction-to-the-nornir-automation-framework/) - David Barroso, Kirk Byers, and Dmitri Figol on Nornir.
-- [Packet Pushers Heavy Networking #498](https://packetpushers.net/podcast/heavy-networking-498-creating-a-single-source-of-truth-for-network-automation/) - Creating A Single Source Of Truth For Network Automation with Tim Schreyack.
+- [Packet Pushers Heavy Networking #498](https://packetpushers.net/podcasts/heavy-networking/hn498-creating-a-single-source-of-truth-for-network-automation/) - Creating A Single Source Of Truth For Network Automation with Tim Schreyack.
 - [Packet Pushers PQ Show 81](https://packetpushers.net/podcast/podcasts/pq-show-81-network-testing-todd/) - Network Testing With ToDD.
 - [Packet Pushers PQ Show 99](https://packetpushers.net/podcast/podcasts/pq-show-99-netmiko-napalm-network-automation/) - Netmiko & NAPALM For Network Automation.
 - [Packet Pushers PQ Show 116](https://packetpushers.net/podcast/podcasts/pq-show-116-practical-yang-network-automation/) - Practical YANG For Network Automation.
```

<details>
<summary>Evidence and limitations</summary>

<p>The episode exists. The old URL redirects to a new canonical URL, and the page confirms the title and guest Tim Schreyack. The description is accurate, so only the URL needs updating.</p>

<p>https://packetpushers.net/podcast/heavy-networking-498-creating-a-single-source-of-truth-for-network-automation/ — Redirects to /podcasts/heavy-networking/HN498-.... rel=canonical and the sitemap give the lowercase hn498 URL.</p>

<p>https://packetpushers.net/podcasts/heavy-networking/hn498-creating-a-single-source-of-truth-for-network-automation/ — Title &#x27;Heavy Networking 498: Creating A Single Source Of Truth For Network Automation&#x27;. Meta: &#x27;Tim Schreyack joins us today to discuss network automation approaches using Ansible and Python, and of course, a single source of truth.&#x27;</p>

</details>

<h3>Cisco Viptela — update</h3>

```diff
--- a/README.md
+++ b/README.md
@@ -539,7 +539,7 @@
 - [Arista CloudVision](https://www.arista.com/en/products/eos/eos-cloudvision) - CloudVision is Arista’s modern, multi-domain management platform that leverages cloud networking principles to deliver a simplified NetOps experience.
 - [Cisco DNA Center](https://developer.cisco.com/dnacenter/) - Cisco DNA Center automates campus networks for faster workflows, faster troubleshooting through more visibility, and policy-driven security (inc. [SDA](https://www.cisco.com/c/en/us/solutions/enterprise-networks/software-defined-access/index.html)).
 - [Cisco Meraki](https://meraki.cisco.com/) - Cisco Meraki is the leader in cloud controlled WiFi, routing, and security. Secure and scalable, Cisco Meraki enterprise networks simply work.
-- [Cisco Viptela](http://viptela.com/) - Viptela provides Software-Defined Wide Area Network (SD-WAN) technology that allows global companies to build cost-effective WANs.
+- [Cisco Catalyst SD-WAN](https://www.cisco.com/site/us/en/solutions/networking/sdwan/index.html) - Cisco Catalyst SD-WAN (formerly Viptela) is Cisco's software-defined WAN solution, with centralized, automated provisioning and management through SD-WAN Manager and its APIs.
 - [Cumulus Networks NetQ](https://cumulusnetworks.com/products/netq/) - Cumulus NetQ is a highly-scalable, modern network operations tool set that provides visibility into your overlay and underlay networks in real-time. NetQ delivers actionable insights and operational intelligence about the health of your data center — from the container, virtual machine, or host, all the way to the switch and port, enabling a NetDevOps approach.
 - [Oracle Talari](https://www.oracle.com/industries/communications/enterprise-communications/products/talari-platforms.html) - Talari Networks SD-WAN technology.
 
```

<details>
<summary>Evidence and limitations</summary>

<p>viptela.com no longer resolves: Google DNS returns no A record for viptela.com and NXDOMAIN for www.viptela.com. Cisco acquired Viptela, and Cisco&#x27;s own release notes state that &#x27;the Cisco SD-WAN solution has been rebranded as Cisco Catalyst SD-WAN&#x27;, with vManage renamed to Cisco Catalyst SD-WAN Manager. This is the same product line under its official current name, not a competitor. Cisco&#x27;s current SD-WAN page emphasizes automated provisioning and management, and DevNet documents the SD-WAN Manager API, which supports the network-automation fit. I recommend a rename with the Cisco URL.</p>

<p>http://viptela.com/ — Proxy returns 502. DNS via dns.google: viptela.com has NOERROR with no A answer (SOA only), and www.viptela.com is NXDOMAIN (Status 3).</p>

<p>https://www.cisco.com/c/en/us/td/docs/routers/sdwan/release/notes/controllers-20-14/rel-notes-controllers-20-14.html — &#x27;To achieve simplification and consistency, the Cisco SD-WAN solution has been rebranded as Cisco Catalyst SD-WAN.&#x27; Lists vManage → Cisco Catalyst SD-WAN Manager, vSmart → Controller, vBond → Validator.</p>

<p>https://www.cisco.com/site/us/en/solutions/networking/sdwan/index.html — Read via WebFetch (curl got HTTP 403): Cisco SD-WAN product page, &#x27;Automate provisioning and management in a single dashboard...&#x27;.</p>

<p>https://developer.cisco.com/docs/sdwan/ — HTTP 200: &#x27;Introduction - Cisco Catalyst SD-WAN Manager API, Release 26.2 - Cisco DevNet&#x27;.</p>

<p>Caveats: Cisco&#x27;s marketing page blocks curl (403) but was readable via WebFetch. Maintainers may prefer the DevNet API docs URL for a more automation-oriented link.; &#x27;Formerly Viptela&#x27; is attested on the Cisco Community forum and by third parties. Cisco&#x27;s release notes confirm the Cisco SD-WAN → Catalyst SD-WAN rename.</p>

<p>Source snapshot incomplete; excluded from the saved baseline.</p>

</details>

<h3>Packet Pushers PQ Show 198 — update</h3>

```diff
--- a/README.md
+++ b/README.md
@@ -563,7 +563,7 @@
 - [Packet Pushers PQ Show 99](https://packetpushers.net/podcast/podcasts/pq-show-99-netmiko-napalm-network-automation/) - Netmiko & NAPALM For Network Automation.
 - [Packet Pushers PQ Show 116](https://packetpushers.net/podcast/podcasts/pq-show-116-practical-yang-network-automation/) - Practical YANG For Network Automation.
 - [Packet Pushers PQ Show 135](https://packetpushers.net/podcast/podcasts/pq-135-mastering-python-networking-book/) - Mastering Python Networking – The Book.
-- [Packet Pushers PQ Show 198](https://packetpushers.net/podcast/podcasts/show-198-kirk-byers-network-automation-python-ansible/) - Kirk Byers on Network Automation with Python & Ansible.
+- [Packet Pushers Show 198](https://packetpushers.net/podcasts/heavy-networking/hn198-kirk-byers-network-automation-python-ansible/) - Kirk Byers on Network Automation with Python & Ansible.
 - [Packet Pushers Show 176](https://packetpushers.net/podcast/podcasts/show-176-intro-to-python-automation-for-network-engineers/) - Intro to Python & Automation for Network Engineers.
 - [Packet Pushers Show 333](https://packetpushers.net/podcast/podcasts/show-333-orchestration-vs-automation/) - Automation & Orchestration In Networking.
 - [Packet Pushers Show 351](https://packetpushers.net/podcast/podcasts/show-351-design-build-13-network-orchestration-salt/) -  Design & Build 13: Network Orchestration with Salt.
```

<details>
<summary>Evidence and limitations</summary>

<p>The old URL returns 404, but the episode exists at a new Packet Pushers URL found in the official sitemap and site search. Its title is &#x27;Show 198 - Kirk Byers on Network Automation with Python &amp; Ansible&#x27;, published 2014-07-28. It was a Packet Pushers Weekly show, now filed under Heavy Networking, not Priority Queue. The entry name &#x27;PQ Show 198&#x27; is therefore wrong. I recommend correcting the name and URL. The description is accurate.</p>

<p>https://packetpushers.net/podcast/podcasts/show-198-kirk-byers-network-automation-python-ansible/ — HTTP 404, no redirect.</p>

<p>https://packetpushers.net/podcasts/heavy-networking/hn198-kirk-byers-network-automation-python-ansible/ — HTTP 200. Title &#x27;Show 198 - Kirk Byers on Network Automation with Python &amp; Ansible | Packet Pushers&#x27;. Meta: &#x27;Packet Pushers Greg Ferro and Ethan Banks discuss network automation with Python expert Kirk Byers.&#x27; datePublished 2014-07-28. Listed in the podcast sitemap.</p>

<p>Source snapshot incomplete; excluded from the saved baseline.</p>

</details>

<h3>Packet Pushers Show 176 — update</h3>

```diff
--- a/README.md
+++ b/README.md
@@ -564,7 +564,7 @@
 - [Packet Pushers PQ Show 116](https://packetpushers.net/podcast/podcasts/pq-show-116-practical-yang-network-automation/) - Practical YANG For Network Automation.
 - [Packet Pushers PQ Show 135](https://packetpushers.net/podcast/podcasts/pq-135-mastering-python-networking-book/) - Mastering Python Networking – The Book.
 - [Packet Pushers PQ Show 198](https://packetpushers.net/podcast/podcasts/show-198-kirk-byers-network-automation-python-ansible/) - Kirk Byers on Network Automation with Python & Ansible.
-- [Packet Pushers Show 176](https://packetpushers.net/podcast/podcasts/show-176-intro-to-python-automation-for-network-engineers/) - Intro to Python & Automation for Network Engineers.
+- [Packet Pushers Show 176](https://packetpushers.net/podcasts/heavy-networking/hn176-intro-to-python-automation-for-network-engineers/) - Intro to Python & Automation for Network Engineers.
 - [Packet Pushers Show 333](https://packetpushers.net/podcast/podcasts/show-333-orchestration-vs-automation/) - Automation & Orchestration In Networking.
 - [Packet Pushers Show 351](https://packetpushers.net/podcast/podcasts/show-351-design-build-13-network-orchestration-salt/) -  Design & Build 13: Network Orchestration with Salt.
 - [Packet Pushers Show 353](https://packetpushers.net/podcast/podcasts/show-353-business-impact-network-automation/) - The Business Impact Of Network Automation.
```

<details>
<summary>Evidence and limitations</summary>

<p>The old URL returns 404, but the same episode is live at a new official URL under Heavy Networking (listed in the sitemap), titled &#x27;Show 176 - Intro to Python &amp; Automation for Network Engineers&#x27;. The description matches, so only the URL needs updating.</p>

<p>https://packetpushers.net/podcast/podcasts/show-176-intro-to-python-automation-for-network-engineers/ — HTTP 404.</p>

<p>https://packetpushers.net/podcasts/heavy-networking/hn176-intro-to-python-automation-for-network-engineers/ — HTTP 200, title &#x27;Show 176 - Intro to Python &amp; Automation for Network Engineers | Packet Pushers&#x27;. Present in the podcast sitemap.</p>

<p>Source snapshot incomplete; excluded from the saved baseline.</p>

</details>

<h3>Packet Pushers Show 333 — update</h3>

```diff
--- a/README.md
+++ b/README.md
@@ -565,7 +565,7 @@
 - [Packet Pushers PQ Show 135](https://packetpushers.net/podcast/podcasts/pq-135-mastering-python-networking-book/) - Mastering Python Networking – The Book.
 - [Packet Pushers PQ Show 198](https://packetpushers.net/podcast/podcasts/show-198-kirk-byers-network-automation-python-ansible/) - Kirk Byers on Network Automation with Python & Ansible.
 - [Packet Pushers Show 176](https://packetpushers.net/podcast/podcasts/show-176-intro-to-python-automation-for-network-engineers/) - Intro to Python & Automation for Network Engineers.
-- [Packet Pushers Show 333](https://packetpushers.net/podcast/podcasts/show-333-orchestration-vs-automation/) - Automation & Orchestration In Networking.
+- [Packet Pushers Show 333](https://packetpushers.net/podcasts/heavy-networking/hn333-orchestration-vs-automation/) - Automation & Orchestration In Networking.
 - [Packet Pushers Show 351](https://packetpushers.net/podcast/podcasts/show-351-design-build-13-network-orchestration-salt/) -  Design & Build 13: Network Orchestration with Salt.
 - [Packet Pushers Show 353](https://packetpushers.net/podcast/podcasts/show-353-business-impact-network-automation/) - The Business Impact Of Network Automation.
 - [Packet Pushers Show 368](https://packetpushers.net/podcast/podcasts/show-368-radical-change-devops-automation/) - Show 368: Radical Change, DevOps & Automation.
```

<details>
<summary>Evidence and limitations</summary>

<p>The old URL returns 404, but the same episode is live at a new official URL under Heavy Networking (listed in the sitemap), titled &#x27;Show 333: Automation &amp; Orchestration In Networking&#x27;. The description matches, so only the URL needs updating.</p>

<p>https://packetpushers.net/podcast/podcasts/show-333-orchestration-vs-automation/ — HTTP 404.</p>

<p>https://packetpushers.net/podcasts/heavy-networking/hn333-orchestration-vs-automation/ — HTTP 200, title &#x27;Show 333: Automation &amp; Orchestration In Networking | Packet Pushers&#x27;. Present in the podcast sitemap.</p>

<p>Source snapshot incomplete; excluded from the saved baseline.</p>

</details>

<h3>Packet Pushers Show 351 — update</h3>

```diff
--- a/README.md
+++ b/README.md
@@ -566,7 +566,7 @@
 - [Packet Pushers PQ Show 198](https://packetpushers.net/podcast/podcasts/show-198-kirk-byers-network-automation-python-ansible/) - Kirk Byers on Network Automation with Python & Ansible.
 - [Packet Pushers Show 176](https://packetpushers.net/podcast/podcasts/show-176-intro-to-python-automation-for-network-engineers/) - Intro to Python & Automation for Network Engineers.
 - [Packet Pushers Show 333](https://packetpushers.net/podcast/podcasts/show-333-orchestration-vs-automation/) - Automation & Orchestration In Networking.
-- [Packet Pushers Show 351](https://packetpushers.net/podcast/podcasts/show-351-design-build-13-network-orchestration-salt/) -  Design & Build 13: Network Orchestration with Salt.
+- [Packet Pushers Show 351](https://packetpushers.net/podcasts/heavy-networking/hn351-design-build-13-network-orchestration-salt/) -  Design & Build 13: Network Orchestration with Salt.
 - [Packet Pushers Show 353](https://packetpushers.net/podcast/podcasts/show-353-business-impact-network-automation/) - The Business Impact Of Network Automation.
 - [Packet Pushers Show 368](https://packetpushers.net/podcast/podcasts/show-368-radical-change-devops-automation/) - Show 368: Radical Change, DevOps & Automation.
 - [Packet Pushers Show 402](https://packetpushers.net/podcast/weekly-show-402-building-a-network-automation-framework/) - Show 402 - Building A Network Automation Framework
```

<details>
<summary>Evidence and limitations</summary>

<p>The old URL returns 404, but the same episode is live at a new official URL under Heavy Networking (listed in the sitemap), titled &#x27;Show 351: Design &amp; Build 13: Network Orchestration with Salt&#x27; (2017, guests Seth House and Mircea Ulinic). The description matches, so only the URL needs updating.</p>

<p>https://packetpushers.net/podcast/podcasts/show-351-design-build-13-network-orchestration-salt/ — HTTP 404.</p>

<p>https://packetpushers.net/podcasts/heavy-networking/hn351-design-build-13-network-orchestration-salt/ — HTTP 200, title &#x27;Show 351: Design &amp; Build 13: Network Orchestration with Salt&#x27;. Meta: &#x27;we discuss Salt. Our use case is that of a network orchestration tool. Our guests are Seth House and Mircea Ulinic.&#x27; datePublished 2017-08-04.</p>

<p>Caveats: The original line has a double space after the separator. That is a cosmetic formatting issue only.</p>

<p>Source snapshot incomplete; excluded from the saved baseline.</p>

</details>

<h3>Packet Pushers Show 353 — update</h3>

```diff
--- a/README.md
+++ b/README.md
@@ -567,7 +567,7 @@
 - [Packet Pushers Show 176](https://packetpushers.net/podcast/podcasts/show-176-intro-to-python-automation-for-network-engineers/) - Intro to Python & Automation for Network Engineers.
 - [Packet Pushers Show 333](https://packetpushers.net/podcast/podcasts/show-333-orchestration-vs-automation/) - Automation & Orchestration In Networking.
 - [Packet Pushers Show 351](https://packetpushers.net/podcast/podcasts/show-351-design-build-13-network-orchestration-salt/) -  Design & Build 13: Network Orchestration with Salt.
-- [Packet Pushers Show 353](https://packetpushers.net/podcast/podcasts/show-353-business-impact-network-automation/) - The Business Impact Of Network Automation.
+- [Packet Pushers Show 353](https://packetpushers.net/podcasts/heavy-networking/HN353-business-impact-network-automation/) - The Business Impact Of Network Automation.
 - [Packet Pushers Show 368](https://packetpushers.net/podcast/podcasts/show-368-radical-change-devops-automation/) - Show 368: Radical Change, DevOps & Automation.
 - [Packet Pushers Show 402](https://packetpushers.net/podcast/weekly-show-402-building-a-network-automation-framework/) - Show 402 - Building A Network Automation Framework
 - [Packet Pushers Show 532](https://packetpushers.net/podcast/heavy-networking-532-scrapli-is-a-netmiko-alternative/) - Scrapli Is A Netmiko Alternative - Show 532 with Carl Montanari and Dmitry Figol.
```

<details>
<summary>Evidence and limitations</summary>

<p>The listed URL returns HTTP 404 (&#x27;Page not found | Packet Pushers&#x27;). The episode now lives at the HN353 URL under /podcasts/heavy-networking/, which returns HTTP 200. Its title, &#x27;Show 353: The Business Impact Of Network Automation&#x27;, matches the entry, and the guest is Alejandro Salinas. The description stays as is; only the URL needs to change.</p>

<p>https://packetpushers.net/podcast/podcasts/show-353-business-impact-network-automation/ — Returns HTTP/2 404, with page title &#x27;Page not found | Packet Pushers&#x27;.</p>

<p>https://packetpushers.net/podcasts/heavy-networking/HN353-business-impact-network-automation/ — HTTP 200. Title: &#x27;Show 353: The Business Impact Of Network Automation | Packet Pushers&#x27;. Description: &#x27;how a major operational change like network automation can impact your organization. Our guest is Alejandro Salinas.&#x27;</p>

<p>Caveats: I didn&#x27;t listen to the audio. I found the new URL by matching the URL pattern Packet Pushers uses for its other migrated episodes, and the page title confirms it&#x27;s the same episode.</p>

<p>Source snapshot incomplete; excluded from the saved baseline.</p>

</details>

<h3>Packet Pushers Show 368 — update</h3>

```diff
--- a/README.md
+++ b/README.md
@@ -568,7 +568,7 @@
 - [Packet Pushers Show 333](https://packetpushers.net/podcast/podcasts/show-333-orchestration-vs-automation/) - Automation & Orchestration In Networking.
 - [Packet Pushers Show 351](https://packetpushers.net/podcast/podcasts/show-351-design-build-13-network-orchestration-salt/) -  Design & Build 13: Network Orchestration with Salt.
 - [Packet Pushers Show 353](https://packetpushers.net/podcast/podcasts/show-353-business-impact-network-automation/) - The Business Impact Of Network Automation.
-- [Packet Pushers Show 368](https://packetpushers.net/podcast/podcasts/show-368-radical-change-devops-automation/) - Show 368: Radical Change, DevOps & Automation.
+- [Packet Pushers Show 368](https://packetpushers.net/podcasts/heavy-networking/HN368-radical-change-devops-automation/) - Show 368: Radical Change, DevOps & Automation.
 - [Packet Pushers Show 402](https://packetpushers.net/podcast/weekly-show-402-building-a-network-automation-framework/) - Show 402 - Building A Network Automation Framework
 - [Packet Pushers Show 532](https://packetpushers.net/podcast/heavy-networking-532-scrapli-is-a-netmiko-alternative/) - Scrapli Is A Netmiko Alternative - Show 532 with Carl Montanari and Dmitry Figol.
 - [Packet Pushers Show 537](https://packetpushers.net/ansible-or-terraform-choose-one/) - Ansible Or Terraform: Choose One with Josh VanDeraa and Ned Bellavance.
```

<details>
<summary>Evidence and limitations</summary>

<p>The listed URL returns HTTP 404. The episode now lives at the HN368 URL, which returns HTTP 200 with the title &#x27;Show 368: Radical Change, DevOps &amp; Automation&#x27;. That matches the entry. The episode discusses automation tooling as a step in network evolution, so it still fits the list. The description stays as is; only the URL needs to change.</p>

<p>https://packetpushers.net/podcast/podcasts/show-368-radical-change-devops-automation/ — Returns HTTP 404, with page title &#x27;Page not found | Packet Pushers&#x27;.</p>

<p>https://packetpushers.net/podcasts/heavy-networking/HN368-radical-change-devops-automation/ — HTTP 200. Title: &#x27;Show 368: Radical Change, DevOps &amp; Automation&#x27;. Description: &#x27;Greg &amp; Ethan discuss why it&#x27;s hard to sell radical products to IT, whether automation tooling is just a step in network evolution &amp; more.&#x27;</p>

<p>Caveats: I didn&#x27;t listen to the audio. The episode is a host discussion, and it is broader than network automation alone.</p>

<p>Source snapshot incomplete; excluded from the saved baseline.</p>

</details>

## Uncertain findings

<h3>Salt Formulas — uncertain</h3>

<details>
<summary>Evidence and limitations</summary>

<p>The Google Group is reachable, but its newest thread is from 4/11/2020. Its welcome text points to a Slack invite (saltstackcommunity.herokuapp.com) that now returns &#x27;No such app&#x27;. Salt Project ended Slack use in 2024. The official Working Groups page still lists an active &#x27;Salt Formulas&#x27; working group (lead Jeff Neel) that meets via Discord #salt-formulas, not this Google Group. The description &#x27;The SaltStack formulas working group&#x27; still names a real group. Unresolved: whether this Google Group is still an official channel of that working group. If not, the official working-groups page or Discord would be the better link.</p>

<p>https://groups.google.com/g/salt-formulas — &#x27;Welcome to the SaltFormulas working group! Click here for a slack invite -&gt; https://saltstackcommunity.herokuapp.com/&#x27;. 19 threads; latest 4/11/20.</p>

<p>https://saltproject.io/community/working-groups/ — Lists the Salt Formulas working group (&#x27;Create pre-written Salt states for common use cases&#x27;, lead Jeff Neel) with the Discord channel #salt-formulas and calendar meeting times. No Google Groups link.</p>

<p>https://saltproject.io/blog/goodbye-slack-hello-discord/ — Salt Project ended Slack use on 2024-03-21 and moved to Discord (https://discord.gg/J7b7EscrAs).</p>

<p>Blocking questions: No official statement found that deprecates the salt-formulas Google Group or names a replacement for it specifically.</p>

<p>Caveats: Low activity alone is not a reason to remove.</p>

<p>Independent source check: Uncertain is appropriate: current working-group page establishes Salt Formulas and Discord context, but does not explicitly retire the Google Group or name an exact replacement. Keep pending; do not infer removal from old activity.</p>

<p>https://saltproject.io/community/working-groups/ — Current working-group listing includes Salt Formulas, Jeff Neel and #salt-formulas.</p>

<p>https://saltproject.io/blog/goodbye-slack-hello-discord/ — Confirms overall Slack migration but not retirement of this specific Google Group.</p>

</details>

<h3>London Network Automation Meetup — uncertain</h3>

<details>
<summary>Evidence and limitations</summary>

<p>The proposed site documents the London meetup and its revival, but neither the original LinkedIn identity nor an official cross-link was independently verified. That missing identity link is material to a URL replacement and belongs in blockers, not merely limitations. A login wall and dated wording alone do not establish a necessary correction.</p>

<p>https://networkautomation.group/ — Title &#x27;London Network Automation Meetup&#x27;. &#x27;LNAM is a volunteer-run meetup focused on hosting periodic meetups in London focused around network automation.&#x27; Next meetup: Wednesday 20 January 2027, Civo Tech Junction, London. Archive: 9 October 2025 talks (MCP servers for network operations, RAG for networks, etc.).</p>

<p>https://networkautomation.group/about/ — &#x27;First organized in 2017 by Csilla Bessenyei and had 14 meetups before taking a hiatus in 2022. A new team of volunteers has resurrected the meetup in 2025.&#x27; Organisers: Pete Crocker, David Gee.</p>

<p>https://www.linkedin.com/company/london-network-automation-meetup/ — HTTP 403 (LinkedIn login wall). Content and ownership could not be read.</p>

<p>https://www.meetup.com/london-network-automation-meetup/ — Meetup.com returns &#x27;Group not found&#x27;.</p>

<p>Blocking questions: The proposed site documents the London meetup and its revival, but neither the original LinkedIn identity nor an official cross-link was independently verified. That missing identity link is material to a URL replacement and belongs in blockers, not merely limitations. A login wall and dated wording alone do not establish a necessary correction.</p>

<p>Caveats: The LinkedIn page may still exist and be maintained. Its status is unknown, not confirmed dead.; networkautomation.group does not link to the LinkedIn page, so the two could not be tied together from official metadata.</p>

<p>Independent source check: The proposed site documents the London meetup and its revival, but neither the original LinkedIn identity nor an official cross-link was independently verified. That missing identity link is material to a URL replacement and belongs in blockers, not merely limitations. A login wall and dated wording alone do not establish a necessary correction.</p>

<p>https://networkautomation.group/ — Live London Network Automation Meetup site and future event.</p>

<p>https://networkautomation.group/about/ — Describes founding in 2017, hiatus in 2022 and revival in 2025; no verified link to the listed LinkedIn page.</p>

</details>

<h3>Minnesota Network User Group — uncertain</h3>

<details>
<summary>Evidence and limitations</summary>

<p>The listed Meetup URL (meetup.com/mn-nug) now returns &#x27;Group not found&#x27;, as does the alternate Meetup slug. The group itself, (MN)NUG, is active under the US Networking User Association (USNUA). A (MN)NUG Minneapolis Fall Event is on Nov 12, 2026, and a Spring 2026 event was on Apr 29, 2026. That suggests semiannual rather than &#x27;quarterly&#x27; meetings. No stable official group page was found to replace the dead link (usnua.com/mnnug returns 404). Fit is also debatable: it is a general networking user group, though some content touches automation.</p>

<p>https://www.meetup.com/mn-nug/ — Meetup.com: &#x27;Group not found – Sorry, the group you&#x27;re looking for doesn&#x27;t exist.&#x27;</p>

<p>https://www.usnua.com/mnnug-minneapolis-fall-event-2026 — USNUA-organized &#x27;(MN)NUG Minneapolis Fall Event&#x27;, November 12, 2026, &#x27;vendor neutral environment to connect and talk networks&#x27;. Keynote &#x27;Agentic Guardrails&#x27;, panel &#x27;Emerging Networking Ideas &amp; Trends&#x27; including an NTC automation consultant.</p>

<p>https://nanog.org/events/mnnug-minnesota-networking-user-group-spring-event-2026/ — Seen via search result: &#x27;(MN)NUG – Minnesota Networking User Group Spring Event 2026&#x27; listed by NANOG (direct fetch blocked by Cloudflare 403).</p>

<p>Blocking questions: No durable official (MN)NUG landing page was found, only per-event USNUA pages, so there is no confirmed replacement URL.; Fit is ambiguous: (MN)NUG is a general networking user group, not network-automation specific. The contribution rules ask maintainers to judge such network-leaning entries.; Meeting cadence (&#x27;quarterly&#x27;) is unconfirmed. Observed 2026 events were spring and fall.</p>

<p>Caveats: A third-party search summary claimed the group no longer uses Meetup and posts events on usnua.com. The linked USNUA join page returned 404, so this could not be confirmed officially.</p>

<p>Independent source check: Independent fetch confirms Meetup group-not-found and an official USNUA event. A stable exact successor and quarterly cadence remain unresolved; holding rather than removing is appropriate.</p>

<p>https://www.meetup.com/mn-nug/ — Responds with Group not found.</p>

<p>https://www.usnua.com/mnnug-minneapolis-fall-event-2026 — Official November12,2026 Minneapolis event includes networking and automation/orchestration topics.</p>

</details>

<h3>Puppetize Live — uncertain</h3>

<details>
<summary>Evidence and limitations</summary>

<p>puppet.com/puppetizelive now 301-redirects to the Puppet homepage (https://www.puppet.com/). puppet.com/events also redirects to the homepage, so no official Puppetize Live page exists anymore. Search history shows Puppetize Live in 2018 and Puppetize PDX in 2019, with no later Puppetize events found. The description presents a current 24-hour global event, which official pages no longer support. However, no explicit official statement that the event was discontinued was found. The entry could be treated as historic or removed. The maintainer should decide whether to drop it or reword it as a historic event, since there is no archive URL to point to.</p>

<p>https://www.puppet.com/ — Destination of the 301 from puppet.com/puppetizelive. The homepage has no Puppetize content.</p>

<p>https://www.puppet.com/community — The official Puppet community page mentions event sponsorship case by case, but no Puppetize or PuppetConf event.</p>

<p>https://www.crunchbase.com/event/puppetize-live-2018 — Seen via search result: Puppetize Live 2018, San Francisco, Oct 9, 2018, a 24-hour global DevOps/automation event, which confirms the event existed historically.</p>

<p>Blocking questions: No explicit official statement found that Puppetize Live / PuppetConf was discontinued. The redirect to the homepage is strong but indirect evidence.; No official archive page (recordings/agenda) was found to repoint the entry as a historic resource.</p>

<p>Caveats: Fit with network automation is indirect (Puppet config management).</p>

<p>Independent source check: Independent HTTP fetch confirms redirect to Puppet homepage, not a current event page. No official discontinuation statement established; uncertain/manual historical treatment remains appropriate.</p>

<p>https://www.puppet.com/puppetizelive — Redirects to https://www.puppet.com/.</p>

<p>https://www.puppet.com/community — Official community material does not by itself establish discontinuation of the historic event.</p>

</details>

<h3>SaltConf — uncertain</h3>

<details>
<summary>Evidence and limitations</summary>

<p>saltconf.com no longer serves SaltConf content. In 2023 it hosted &#x27;SaltConf21&#x27;, a free virtual event, not the 4-day event described. Wayback captures since 2025 are tiny pages, and in 2026 the page is a JavaScript redirect to &#x27;/lander&#x27;, which looks like a parked domain. Live fetches returned a 502 from the proxy, so I could not confirm the current state directly. I found no official Salt Project announcement of a current SaltConf or of its discontinuation.</p>

<p>https://web.archive.org/web/20230530053338/https://saltconf.com/ — The 2023 snapshot is titled &#x27;SaltConf21 - SaltConf&#x27;, with &#x27;Register for FREE&#x27;, labs, contests and &#x27;Past SaltConf Videos&#x27;. It describes a gathering with hands-on training and education.</p>

<p>https://web.archive.org/web/20260830235729/https://saltconf.com/ — The August 2026 capture is about 577 bytes and contains only a script redirecting to &#x27;/lander&#x27;, a typical parked-domain pattern.</p>

<p>https://saltproject.io/ — The Salt Project site is live. A web search found no SaltConf 2026 event, only unrelated &#x27;SALT&#x27; conferences.</p>

<p>Blocking questions: Domain ownership and parking status are unconfirmed because the live site was unreachable from here.; No official archive of past SaltConf talks was verified, so I cannot propose a historic replacement URL.; The &#x27;4 days event&#x27; wording is already outdated against SaltConf21 (a free virtual event), but the right fix depends on whether the entry is kept at all.</p>

<p>Caveats: The live saltconf.com fetch failed with a proxy 502, which may be environmental.</p>

<p>Source snapshot incomplete; excluded from the saved baseline.</p>

</details>

<h3>Network Programmability Basics - Cisco — uncertain</h3>

<details>
<summary>Evidence and limitations</summary>

<p>The official course page developer.cisco.com/video/net-prog-basics/ and its module subpages return 404. Wayback shows HTTP 200 through December 2025, then 404 or redirects from April 2026. I found no official Cisco page naming a new home for the course. Its companion GitHub repository (CiscoDevNet/netprog_basics) still exists. The videos also appear on the Cisco DevNet YouTube channel, but the 28-video playlist found was created by a third party, not Cisco.</p>

<p>https://developer.cisco.com/video/net-prog-basics/ — Fetched 2026-11-10 with HTTP 404. Module URLs such as /02-network_device_apis/ also return 404.</p>

<p>https://web.archive.org/web/20251214135923/https://developer.cisco.com/video/net-prog-basics/ — The CDX index shows HTTP 200 captures through 2025-12-14, then 404 and 301 captures from 2026-04-13.</p>

<p>https://github.com/CiscoDevNet/netprog_basics — The repo is live: &#x27;Code, Examples, and Resources for the Network Programmability Basics Video Course&#x27;. Its README lists the modules.</p>

<p>https://www.youtube.com/playlist?list=PLCTifDArWwqLrJQf_0vvM2u7Kwx84qsWD — The &#x27;Cisco DevNet Network Programmability Basics Course&#x27; playlist has 28 videos uploaded by @CiscoDevNetchannel, but the playlist was created by Mohammed Khalefa, not Cisco.</p>

<p>Blocking questions: I found no official Cisco destination for the video course. The GitHub repo holds code rather than the videos, and the YouTube playlist is not Cisco-curated, so a replacement URL cannot be confirmed.; It is unknown whether Cisco intentionally retired the course or moved it to another DevNet or Cisco U. location.</p>

<p>Caveats: The GitHub API returned no metadata for the repo, so its archive status is unknown.</p>

<p>Source snapshot incomplete; excluded from the saved baseline.</p>

</details>

<h3>Packet Life — uncertain</h3>

<details>
<summary>Evidence and limitations</summary>

<p>packetlife.net did not resolve from two independent fetchers (proxy 502 and ENOTFOUND). Third-party reports say it has been offline since late summer 2024 with no explanation from Jeremy Stretch. I found no official statement of retirement or of a successor site. Separately, the description &#x27;Network Automation thoughts&#x27; looks inaccurate for a site best known for networking cheat sheets, but I could not confirm that from the live site.</p>

<p>http://packetlife.net/ — HTTP 502 from the proxy, and WebFetch reports getaddrinfo ENOTFOUND for packetlife.net. Local DNS resolution also failed.</p>

<p>http://web.archive.org/web/20241002022649/https://packetlife.net/ — The Wayback availability API&#x27;s latest snapshot is 2024-10-02. A 2026 query redirected to that snapshot.</p>

<p>https://theitcave.com/post/58/ — A third-party post (from search results) says PacketLife.net went offline in late summer 2024, that the reason is unknown, and that the author has not commented.</p>

<p>Blocking questions: No official statement from Jeremy Stretch about whether packetlife.net is permanently retired.; Whether the site&#x27;s content counts as network automation rather than general networking is unresolved without live access.</p>

<p>Caveats: The DNS failure could be partly environmental, although it was reproduced with two independent fetchers.; Third-party sources are not official evidence of retirement.</p>

<p>Source snapshot incomplete; excluded from the saved baseline.</p>

</details>

<h3>Wim Wauters — uncertain</h3>

<details>
<summary>Evidence and limitations</summary>

<p>blog.wimwauters.com did not resolve (proxy 502, WebFetch ENOTFOUND). The latest Wayback snapshot I found (Aug 2024) shows a &#x27;Technology Blog Wim&#x27; with a Network Programmability category, which supported the fit at that time. I found no official notice of the blog&#x27;s status or a new location.</p>

<p>https://blog.wimwauters.com/categories/all/ — The CONNECT tunnel failed (502), and WebFetch reports getaddrinfo ENOTFOUND blog.wimwauters.com.</p>

<p>http://web.archive.org/web/20240812221807/https://blog.wimwauters.com/ — The 2024-08-12 snapshot is titled &#x27;Technology Blog Wim&#x27;, with categories including Network Programmability, DevOps and Cloud. The latest posts are Pulumi/AWS articles from April 2022.</p>

<p>http://web.archive.org/web/20250521084135/https://blog.wimwauters.com/categories/all/ — The Wayback availability API shows a 200 snapshot of the listed URL as late as 2025-05-21, so the outage is recent.</p>

<p>Blocking questions: It is unknown whether the domain lapsed permanently or the blog moved to a new official URL.</p>

<p>Caveats: The DNS failure may be temporary or environmental and should be rechecked.; I did not search for a relocated blog.</p>

<p>Source snapshot incomplete; excluded from the saved baseline.</p>

</details>

<h3>Getting Started and Basics — uncertain</h3>

<details>
<summary>Evidence and limitations</summary>

<p>The listed URL for the legacy Codecademy course &#x27;Meet JSON&#x27; (JavaScript beginner track) now returns 404 from codecademy.com. The Wayback Machine has a 2018 capture titled &#x27;Meet JSON | Codecademy&#x27;. I found no official redirect or documented successor, so I cannot recommend a replacement URL. A 404 alone is not official evidence of removal, so remove is not justified either.</p>

<p>https://www.codecademy.com/courses/javascript-beginner-en-xTAfX/0/1 — Returns HTTP 404 with the generic title &#x27;Codecademy from Skillsoft&#x27;.</p>

<p>http://web.archive.org/web/20180502145403/https://www.codecademy.com/courses/javascript-beginner-en-xTAfX/0/1 — The archived capture&#x27;s title is &#x27;Meet JSON | Codecademy&#x27;, which shows the original was a JSON-basics lesson.</p>

<p>https://www.codecademy.com/article/what-is-json — This URL returns 200 and may be a current Codecademy JSON article, but I could not extract its content. It is not documented as a successor to the course.</p>

<p>Blocking questions: No officially documented successor for the removed &#x27;Meet JSON&#x27; lesson. The candidate codecademy.com/article/what-is-json is unverified as a replacement and its content was not read.; Unknown whether Codecademy retired the lesson for good or moved it to an unknown URL.</p>

<p>Caveats: Codecademy pages are heavily JavaScript-rendered, so content extraction was limited.</p>

<p>Source snapshot incomplete; excluded from the saved baseline.</p>

</details>

<h3>Python Programming Guides and Tutorials - Python Central — uncertain</h3>

<details>
<summary>Evidence and limitations</summary>

<p>The site is live and still has Python tutorials, recipes, and library guides. Two things are unresolved. First, the description&#x27;s claim of &#x27;experienced Python programmers and enthusiasts from around the world&#x27; is not supported: the About page says one person (Jackson Cooper of Aztech Media) built and maintains the site. Second, the homepage and About page now include off-topic sponsored or spam content, which makes it unclear whether this is still a curated learning resource worth keeping. A maintainer should decide whether it still fits before any wording change.</p>

<p>https://www.pythoncentral.io/about/ — About page: &#x27;The website was built and is maintained by Jackson Cooper of Aztech Media.&#x27; It describes the site as content for beginner, intermediate and advanced Python developers. The page body also contains an unrelated injected phrase, &#x27;rolex oyster perpetual milgauss fake vs real&#x27;.</p>

<p>https://www.pythoncentral.io/ — pythoncentral.io redirects here (HTTP 200). The page has tutorials (SQLAlchemy, Django, PySide, SQLite) and recipes. The &#x27;Python Programming Guides and Tutorials&#x27; block lists crypto-wallet posts (&#x27;How to Update Ledger Live Fast and Without Risks&#x27;, &#x27;Ledger Live Security Risks…&#x27;). Other sections include unrelated business/SaaS posts.</p>

<p>Blocking questions: Unclear whether the off-topic and apparently injected content means the site no longer works as a trustworthy Python learning resource; this needs a maintainer decision.; If kept, the description needs rewording (e.g. &#x27;Python tutorials, recipes and library guides&#x27;), but that depends on the relevance decision.</p>

<p>Caveats: Did not review individual articles for quality or dates.; Whether the off-topic posts are paid placements or a compromise is unknown.</p>

</details>

<h3>Infoblox Perl API — uncertain</h3>

<details>
<summary>Evidence and limitations</summary>

<p>Both linked hosts appear to be gone. demogm1.infoblox.com returns NXDOMAIN from Cloudflare and Google DNS-over-HTTPS (the infoblox.com zone answers authoritatively), the sandbox proxy returned 502, and the Wayback CDX has no captures. That points to a decommissioned demo Grid Master, not a transient failure, but DNS absence is still access evidence rather than an official statement. Infoblox officially says the Perl API (PAPI) has been deprecated since NIOS 8.3 and that WAPI is the supported REST API. WAPI docs are published as a PDF on docs.infoblox.com, plus each appliance&#x27;s /wapidoc. The compound line is non-editable, so the maintainer must choose new destinations: probably drop the Perl API link and point the REST link at the official WAPI reference.</p>

<p>https://cloudflare-dns.com/dns-query?name=demogm1.infoblox.com&amp;type=A — Status 3 (NXDOMAIN), with an SOA authority from the infoblox.com zone. Google DNS (https://dns.google/resolve?name=demogm1.infoblox.com&amp;type=A) also returns Status 3.</p>

<p>https://web.archive.org/cdx/search/cdx?url=demogm1.infoblox.com/wapidoc/&amp;output=json — Empty result: no archived captures for /wapidoc/ or /api/doc/.</p>

<p>https://infoblox-docs.atlassian.net/wiki/spaces/nios90/pages/156664532/Using+NIOS+APIs — &#x27;The Perl API (PAPI) for NIOS has been deprecated from NIOS 8.3 onwards. Infoblox recommends that you migrate to WAPI&#x27; and &#x27;All enhancements and fixes for NIOS APIs are provided through WAPI from NIOS 8.4 onwards.&#x27; Detailed API info is in a PDF on docs.infoblox.com.</p>

<p>https://docs.infoblox.com/space/nios90/ — The official NIOS 9.0 documentation space is reachable (200). A web search surfaced the &#x27;Infoblox NIOS WAPI 9.x Reference Guide&#x27; PDF under docs.infoblox.com/download/attachments/15433773/, which I did not open.</p>

<p>Blocking questions: No official notice explicitly retires demogm1.infoblox.com. Its absence is inferred from NXDOMAIN and missing archives.; The successor link is a maintainer choice: the versioned WAPI PDF reference guide or the docs.infoblox.com &#x27;Using NIOS APIs&#x27; page. A public appliance-hosted /wapidoc mirror (e.g. a university&#x27;s) is not an Infoblox-owned destination.</p>

<p>Caveats: The DNS lookups went through public DoH resolvers, not Infoblox&#x27;s authoritative servers. The host could exist on internal or split-horizon DNS.; The entry is a non-editable compound line, so no patch fields are supplied.</p>

<p>Source snapshot incomplete; excluded from the saved baseline.</p>

</details>

<h3>SaltStack fundamentals — uncertain</h3>

<details>
<summary>Evidence and limitations</summary>

<p>The SaltStack &#x27;Get Started&#x27; fundamentals guide returns 404 on both docs.saltstack.com and docs.saltproject.io/en/getstarted/fundamentals/. The Wayback Machine shows it was live on docs.saltproject.io until at least October 2024, with the entry&#x27;s wording. Today the closest official material is the Salt User Guide (docs.saltproject.io/salt/user-guide/en/latest/), but I found no official statement that it replaces the Get Started guides. A replacement URL therefore cannot be confirmed.</p>

<p>https://docs.saltstack.com/en/getstarted/fundamentals/ — HTTP 404.</p>

<p>https://docs.saltproject.io/en/getstarted/fundamentals/ — HTTP 404.</p>

<p>http://web.archive.org/web/20241001021728/https://docs.saltproject.io/en/getstarted/fundamentals/ — Archived 2024-10-01: &#x27;SaltStack Fundamentals – This Getting Started Guide walks you through the fundamental concepts you need to learn as you start using SaltStack&#x27; (install, remote execution, targeting, states).</p>

<p>https://docs.saltproject.io/salt/user-guide/en/latest/ — HTTP 200. The Salt User Guide covers overview, installation, states, pillar, targeting, salt-ssh and similar topics. It is a possible alternative but not documented as the successor.</p>

<p>Blocking questions: No official redirect or announcement was found naming a successor to the retired Get Started fundamentals guide. Pointing to the Salt User Guide or to the Wayback archive is a maintainer judgement.</p>

<p>Caveats: The guide is generic Salt learning material in the Salt section and has no network-specific content.</p>

<p>Source snapshot incomplete; excluded from the saved baseline.</p>

</details>

<h3>SaltStack configuration management — uncertain</h3>

<details>
<summary>Evidence and limitations</summary>

<p>The SaltStack &#x27;Get Started&#x27; configuration management guide returns 404 on both docs.saltstack.com and docs.saltproject.io/en/getstarted/config/. Wayback has a 2024-10-01 snapshot of the saltproject.io copy. No officially documented successor page was found; the Salt User Guide&#x27;s states material is the closest candidate.</p>

<p>https://docs.saltstack.com/en/getstarted/config/ — HTTP 404.</p>

<p>https://docs.saltproject.io/en/getstarted/config/ — HTTP 404.</p>

<p>https://archive.org/wayback/available?url=docs.saltproject.io/en/getstarted/config/ — Closest snapshot: status 200 at http://web.archive.org/web/20241001021358/https://docs.saltproject.io/en/getstarted/config/.</p>

<p>https://docs.saltproject.io/salt/user-guide/en/latest/ — HTTP 200. Contains topics such as states.html, state-system.html and requisites.html, but is not documented as the successor of the Get Started config guide.</p>

<p>Blocking questions: No official successor URL for the retired Get Started configuration management guide was found. Choosing between the User Guide, an archive link, or removal needs a maintainer decision.</p>

<p>Caveats: Did not read the archived config guide&#x27;s body in detail; only its availability was confirmed.</p>

<p>Source snapshot incomplete; excluded from the saved baseline.</p>

</details>

<h3>Network Automation at Scale — uncertain</h3>

<details>
<summary>Evidence and limitations</summary>

<p>The listed O&#x27;Reilly &#x27;.csp&#x27; free-ebook URL now redirects to the O&#x27;Reilly library page (ISBN 9781491992524), which returned 403 to automated clients. I could not confirm whether the book is still free from O&#x27;Reilly. Library pages are normally subscription-gated, so the &#x27;free ebook from O&#x27;Reilly&#x27; claim may be outdated. Cloudflare hosts a page offering the same book as a free download behind a form. The book&#x27;s content (Salt-based network automation by Ulinic and House) is still relevant.</p>

<p>https://www.oreilly.com/webops-perf/free/network-automation-at-scale.csp — curl followed redirects to https://www.oreilly.com/library/view/~/9781491992524, which returned 403. I saw no evidence of a free-download landing page remaining at O&#x27;Reilly.</p>

<p>https://www.cloudflare.com/network-automation-at-scale-ebook/ — Live page titled &#x27;Free eBook: Network Automation at Scale | Cloudflare&#x27;. It describes the Ulinic/House book on Salt, NAPALM and Jinja/YAML and has a download form.</p>

<p>https://www.oreilly.com/library/view/network-automation-at/9781491992524/ch06.html — A search result shows the book&#x27;s chapters (&#x27;The Salt Event Bus&#x27;) in O&#x27;Reilly&#x27;s library under the ISBN path.</p>

<p>Blocking questions: Whether O&#x27;Reilly still offers the ebook for free at the redirect target is unverified.; Whether the Cloudflare download page counts as an acceptable official replacement link (it is the authors&#x27; former employer and sponsor, and is gated by a lead form) needs a maintainer decision.</p>

<p>Caveats: O&#x27;Reilly blocks automated fetches, so I could not see the redirect target&#x27;s content.</p>

<p>Source snapshot incomplete; excluded from the saved baseline.</p>

</details>

<h3>NetYCE — uncertain</h3>

<details>
<summary>Evidence and limitations</summary>

<p>netyce.com now redirects to netpicker.io. Netpicker is a separate network testing, compliance and automation product from the same team, now under the Flock9 brand. I found no official statement that the NetYCE &#x27;Design Driven Networking&#x27; product was renamed, discontinued or succeeded by Netpicker. Netpicker&#x27;s support site still hosts NetYCE knowledge-base articles. This entry is also not editable (malformed line with the link duplicated inside the description), so any change needs manual handling.</p>

<p>https://netyce.com/ — Redirects (1 hop) to https://netpicker.io/.</p>

<p>https://netpicker.io/ — Netpicker describes itself as network testing: &#x27;Continuously validate real network state before and after changes. Test configs, compliance, security, and network behavior. Automate remediation.&#x27; It is built on Python and pytest, supports 180+ vendors, and makes no mention of NetYCE or Design Driven Networking on the homepage.</p>

<p>https://support.netpicker.io/support/solutions/articles/201000077460-how-to-verify-and-update-netyce-software — Search result shows a NetYCE software-update knowledge-base article on Netpicker&#x27;s support portal, which suggests NetYCE is still supported. I did not read it directly.</p>

<p>Blocking questions: No official evidence that Netpicker is the documented successor to the NetYCE product, or that NetYCE is discontinued.; The entry is marked non-editable because the line is malformed.</p>

<p>Caveats: A Packet Pushers podcast (NAN087) reportedly says the NetYCE founders started Netpicker as a new modular product. That is secondary and not an official successor notice.</p>

</details>

<h3>Anuta Networks ATOM — uncertain</h3>

<details>
<summary>Evidence and limitations</summary>

<p>www.anutanetworks.com fails a TLS handshake for both curl and WebFetch, and http://anutanetworks.com returns a Cloudflare 1001/409 error. I could not read any official Anuta page. Search results show no acquisition, and the company still appears active in third-party company databases, but I could not confirm that ATOM is still offered or that the description is accurate.</p>

<p>Blocking questions: No official Anuta source could be read to confirm the product&#x27;s current status or URL.</p>

<p>Caveats: The failures look like TLS/DNS configuration problems, which could be temporary. Recheck before acting.; Secondary sources (Tracxn, BusinessWire 2018–2021) describe ATOM as a multi-vendor assurance, telemetry and orchestration platform. I did not read them directly here.</p>

<p>Source snapshot incomplete; excluded from the saved baseline.</p>

</details>

<h3>Oracle Talari — uncertain</h3>

<details>
<summary>Evidence and limitations</summary>

<p>The listed Oracle product URL now 2-hop redirects to Oracle&#x27;s generic Communications landing page, so it no longer documents Talari. Oracle&#x27;s Talari Platforms documentation is still online, but it was last modified in May 2022. Third-party sources say the product is discontinued, but I found no public official end-of-life notice. Oracle&#x27;s support-policy document does carry Talari-specific hardware support terms. Fit is also borderline: this is an SD-WAN product, and its network-automation value is not evident from the remaining sources. The maintainer should decide whether to point the entry at the docs page or drop it. I can&#x27;t confirm removal from official evidence.</p>

<p>https://www.oracle.com/industries/communications/enterprise-communications/products/talari-platforms.html — Redirects (2 hops) to https://www.oracle.com/communications/, a generic page with no Talari product content.</p>

<p>https://docs.oracle.com/en/industries/communications/talari-platform/index.html — HTTP 200 &#x27;Oracle Talari Platforms - Home&#x27;, describing Talari SD-WAN appliances (physical, virtual, cloud). Metadata: datePublished 2019-11-01, dateModified 2022-05-20.</p>

<p>https://www.oracle.com/contracts/docs/hardware-systems-support-policies-069182.pdf — Search summary (I did not read the PDF directly) says Oracle&#x27;s hardware support policy limits support for Talari SD-WAN hardware to three years from Last Ship Date. That is not an explicit EOL notice.</p>

<p>https://packetpushers.net/blog/sd-wan-vendors-sase-vendors/ — Third-party (search summary) says Oracle SD-WAN appears to be a dead product, with the last docs release 9.1 in September 2022. This is not official evidence.</p>

<p>Blocking questions: No official public end-of-sale/end-of-life statement was found for Talari SD-WAN.; Network-automation fit of a discontinued-looking SD-WAN product is ambiguous and needs a maintainer decision.</p>

<p>Caveats: The Last Ship Dates in My Oracle Support (Doc ID 1450710.1) require a login and were not checked.</p>

</details>

<h3>Network to Code — uncertain</h3>

<details>
<summary>Evidence and limitations</summary>

<p>I could not read networkcollective.com from this environment: the proxy returned CONNECT 502 and WebFetch got connection refused, even though DNS resolves (13.248.169.48, 76.223.54.146). A Wayback snapshot from Sept 2021 of the category URL exists. Search results show the &#x27;NTC –&#x27; episodes (2020: Source of Truth, Security and Networking, Jason Edelman, Damien Garros) are network-automation content, and that the Apple Podcasts feed is now titled &#x27;Underlay&#x27;. I can&#x27;t tell whether the site is temporarily unreachable or gone, so this needs a recheck rather than removal.</p>

<p>https://networkcollective.com/category/episodes/network-to-code/ — curl: proxy CONNECT tunnel failed (502). WebFetch: ECONNREFUSED. dns.google resolves A records 13.248.169.48 and 76.223.54.146.</p>

<p>http://web.archive.org/web/20210924002754/https://networkcollective.com/category/episodes/network-to-code/ — Wayback availability API reports a 200 snapshot from 2021-09-24 (contents not read).</p>

<p>https://podcasts.apple.com/us/podcast/ntc-source-of-truth/id1223814895?i=1000468132977 — Search result shows NTC episodes in the same Apple feed, now titled &#x27;Underlay&#x27;. Not read directly.</p>

<p>Blocking questions: Current reachability of networkcollective.com is unknown from this environment. It may be a local network restriction or an actual outage.</p>

<p>Caveats: Search results suggest the last Network Collective post was in January 2022. Inactivity alone does not justify removal.</p>

<p>Source snapshot incomplete; excluded from the saved baseline.</p>

</details>

<h3>Network Collective EPISODE 10 — uncertain</h3>

<details>
<summary>Evidence and limitations</summary>

<p>The listed host thenetworkcollective.com now returns HTTP 404 for this path and for its root (&#x27;404 - Page not found&#x27;), so the link is broken. Wayback shows the same episode was later published at https://networkcollective.com/2017/08/ep10-grassroots-automation/ (2021 snapshot). That domain was not reachable from this environment, so I could not verify it as a working replacement URL. The topic (grassroots network automation) fits.</p>

<p>https://thenetworkcollective.com/2017/08/ep10-grassroots-automation/ — HTTP 404 after one redirect. The site root also returns &#x27;404 - Page not found&#x27;.</p>

<p>http://web.archive.org/web/20210920231024/https://networkcollective.com/2017/08/ep10-grassroots-automation/ — Wayback availability API reports a 200 snapshot of the same slug on networkcollective.com from 2021-09-20, suggesting this is the canonical domain.</p>

<p>http://web.archive.org/web/20240423111136/http://thenetworkcollective.com/2017/08/ep10-grassroots-automation/ — Wayback availability API reports a 200 snapshot of the listed URL from 2024-04-23. The page title was not readable.</p>

<p>Blocking questions: The candidate URL https://networkcollective.com/2017/08/ep10-grassroots-automation/ could not be fetched live (connection refused / proxy 502), so it is unverified as a working destination.</p>

<p>Caveats: Historic episode, so its age is not a concern.</p>

<p>Source snapshot incomplete; excluded from the saved baseline.</p>

</details>

<h3>Network Collective Infrastructure as Code 101 — uncertain</h3>

<details>
<summary>Evidence and limitations</summary>

<p>I could not reach networkcollective.com live (proxy 502 / connection refused). A Wayback snapshot (Dec 2021) confirms the page title &#x27;Infrastructure As Code 101 » Network Collective&#x27; and mentions Garros and Celenza, so the description is historically accurate. Current availability is unresolved. The entry is not editable and lacks the &#x27; - &#x27; separator. That formatting is not a factual error.</p>

<p>https://networkcollective.com/2019/09/infrastructure-as-code/ — curl: proxy CONNECT tunnel failed (502). The domain resolves via dns.google.</p>

<p>http://web.archive.org/web/2021/https://networkcollective.com/2019/09/infrastructure-as-code/ — Archived page title &#x27;Infrastructure As Code 101 » Network Collective&#x27;. Page contains &#x27;Garros&#x27; and &#x27;Celenza&#x27;.</p>

<p>Blocking questions: Live reachability of networkcollective.com is unknown from this environment.</p>

<p>Caveats: The entry is marked non-editable in the packet.</p>

<p>Source snapshot incomplete; excluded from the saved baseline.</p>

</details>

<h3>Packet Pushers Datanauts 80 — uncertain</h3>

<details>
<summary>Evidence and limitations</summary>

<p>The listed URL returns 404. I found no current location: the Datanauts series is absent from all four Packet Pushers podcast sitemaps (3,195 URLs; current shows include heavy-networking, day-two-devops, full-stack-journey, etc.), /podcasts/datanauts/ returns 404, and guessed slugs return 404. Wayback has a 2017 snapshot titled &#x27;Datanauts 080: The Current State Of Network Automation &amp; Telemetry&#x27;, which confirms the description historically. There is no official redirect or successor page, and no official statement that the episode was withdrawn. Options are an archive URL or removal, both maintainer decisions.</p>

<p>https://packetpushers.net/podcast/podcasts/datanauts-080-network-automation-telemetry/ — HTTP 404, no redirect.</p>

<p>https://packetpushers.net/podcast-sitemap.xml — Podcast sitemaps 1–4 list 3,195 episode URLs. None are in a Datanauts category, and no URL matches datanauts/dn080. /podcasts/datanauts/ returns 404.</p>

<p>http://web.archive.org/web/20171118195827/http://packetpushers.net/podcast/podcasts/datanauts-080-network-automation-telemetry/ — Archived 200 page titled &#x27;Datanauts 080: The Current State Of Network Automation &amp; Telemetry - Packet Pushers&#x27;.</p>

<p>Blocking questions: No official current URL found. Whether to use a Wayback link or drop the entry is a maintainer policy decision.</p>

<p>Caveats: The audio may still be distributed via podcast directories. I did not check them.</p>

<p>Source snapshot incomplete; excluded from the saved baseline.</p>

</details>

<h3>Packet Pushers PQ Show 81 — uncertain</h3>

<details>
<summary>Evidence and limitations</summary>

<p>The listed URL returns 404. The Priority Queue series does not appear in Packet Pushers&#x27; current podcast sitemaps, and guessed new-style slugs (/podcasts/priority-queue/pq081-…) return 404. Wayback confirms the original title &#x27;PQ Show 81: Network Testing With ToDD&#x27;. There is no official current page and no official removal statement.</p>

<p>https://packetpushers.net/podcast/podcasts/pq-show-81-network-testing-todd/ — HTTP 404.</p>

<p>https://packetpushers.net/podcast-sitemap.xml — No priority-queue category or matching ToDD episode among the 3,195 sitemap podcast URLs.</p>

<p>http://web.archive.org/web/20171118195314/http://packetpushers.net/podcast/podcasts/pq-show-81-network-testing-todd/ — Archived page title &#x27;PQ Show 81: Network Testing With ToDD&#x27;.</p>

<p>Blocking questions: No official current URL found. An archive link or removal needs a maintainer decision.</p>

<p>Caveats: Third-party directories (e.g. Player.fm lists Priority Queue as an archived series) may still host the audio. I did not verify them as official.</p>

<p>Source snapshot incomplete; excluded from the saved baseline.</p>

</details>

<h3>Packet Pushers PQ Show 99 — uncertain</h3>

<details>
<summary>Evidence and limitations</summary>

<p>The listed URL returns 404. Priority Queue is absent from Packet Pushers&#x27; current sitemaps. Search shows the episode (Nov 2016, Kirk Byers on Netmiko and NAPALM) on Player.fm&#x27;s archived &#x27;Packet Pushers - Priority Queue&#x27; series, and Wayback has a 2018 snapshot. There is no official current page.</p>

<p>https://packetpushers.net/podcast/podcasts/pq-show-99-netmiko-napalm-network-automation/ — HTTP 404.</p>

<p>http://web.archive.org/web/20180623004225/http://packetpushers.net:80/podcast/podcasts/pq-show-99-netmiko-napalm-network-automation/ — Wayback availability API reports a 200 snapshot from 2018-06-23.</p>

<p>https://player.fm/series/packet-pushers-priority-queue/pq-show-99-netmiko-napalm-for-network-automation — Search result: &#x27;PQ Show 99: Netmiko &amp; NAPALM For Network Automation&#x27; in the archived Priority Queue series. This is a third-party directory, not read directly.</p>

<p>Blocking questions: No official current URL found. A third-party directory or Wayback link would be a maintainer choice.</p>

<p>Source snapshot incomplete; excluded from the saved baseline.</p>

</details>

<h3>Packet Pushers PQ Show 116 — uncertain</h3>

<details>
<summary>Evidence and limitations</summary>

<p>The listed URL returns 404, and there is no current Packet Pushers page (Priority Queue is absent from the sitemaps; guessed slug 404). Wayback confirms the title &#x27;PQ Show 116: Practical YANG For Network Automation&#x27;.</p>

<p>https://packetpushers.net/podcast/podcasts/pq-show-116-practical-yang-network-automation/ — HTTP 404.</p>

<p>http://web.archive.org/web/20180606212251/http://packetpushers.net:80/podcast/podcasts/pq-show-116-practical-yang-network-automation/ — Archived page title &#x27;PQ Show 116: Practical YANG For Network Automation - Packet Pushers&#x27;.</p>

<p>https://packetpushers.net/podcast-sitemap.xml — No priority-queue entries in the current podcast sitemaps.</p>

<p>Blocking questions: No official current URL found. An archive link or removal needs a maintainer decision.</p>

<p>Source snapshot incomplete; excluded from the saved baseline.</p>

</details>

<h3>Packet Pushers PQ Show 135 — uncertain</h3>

<details>
<summary>Evidence and limitations</summary>

<p>The listed URL returns 404, and there is no current Packet Pushers page for PQ 135. Wayback confirms the title &#x27;PQ 135: Mastering Python Networking - The Book&#x27;. Packet Pushers does host a later, different episode on the third edition (Tech Bytes TB088, Eric Chou), but that is a different episode and not a documented successor.</p>

<p>https://packetpushers.net/podcast/podcasts/pq-135-mastering-python-networking-book/ — HTTP 404.</p>

<p>http://web.archive.org/web/20180623003535/http://packetpushers.net:80/podcast/podcasts/pq-135-mastering-python-networking-book/ — Archived page title &#x27;PQ 135: Mastering Python Networking - The Book - Packet Pushers&#x27;.</p>

<p>https://packetpushers.net/podcasts/tech-bytes/tb088-mastering-python-networking-third-edition-by-eric-chou/ — A different, later episode on the book&#x27;s third edition appeared in search. It is not a replacement for PQ 135.</p>

<p>Blocking questions: No official current URL found for PQ 135. TB088 is a different episode and would be a new entry, not an update.</p>

<p>Source snapshot incomplete; excluded from the saved baseline.</p>

</details>

<details>
<summary>56 unresolved keeps</summary>

These entries were not added to the baseline.

<h3>Infrahub Community — keep</h3>

<p>Source or catalog stability was not confirmed for this review.</p>

<details>
<summary>Evidence and limitations</summary>

<p>The discord.gg/opsmill invite redirects to discord.com/invite/opsmill and resolves to the &#x27;OpsMill&#x27; guild, described as &#x27;OpsMill Community https://opsmill.com&#x27;. OpsMill makes Infrahub, and the invite does not expire. The server matches the description of an Infrahub user community.</p>

<p>https://discord.com/api/v9/invites/opsmill?with_counts=true — Invite resolves to guild &#x27;OpsMill&#x27; (COMMUNITY feature enabled), description &#x27;OpsMill Community https://opsmill.com&#x27;, expires_at null, about 585 members (about 94 online) at check time.</p>

<p>Caveats: Could not see channel contents without joining, so the Infrahub-specific discussion was not observed directly.</p>

<p>Independent source check: Independent official Infrahub documentation and repository README explicitly identify this Discord as the Infrahub community/support channel, resolving the model’s weak metadata-only linkage. Joining private channels is not necessary to establish advertised purpose.</p>

<p>https://docs.infrahub.app/faq — Official FAQ identifies Discord as the place to engage with Infrahub users and developers.</p>

<p>https://github.com/opsmill/infrahub/blob/stable/README.md — Official README links discord.gg/opsmill under community and support.</p>

</details>

<h3>Network to Code Slack — keep</h3>

<p>Source or catalog stability was not confirmed for this review.</p>

<details>
<summary>Evidence and limitations</summary>

<p>Over 17,000 remains mathematically true when membership exceeds 35,000. Removing NSoT is explicitly admitted by the model to be editorial, with no channel inspection. HTTPS redirect cleanup is optional. This is not a supported necessary freshness correction; do not advertise it or accept the compound edit.</p>

<p>https://slack.networktocode.com/ — Live Slack self-signup page: &#x27;Enter your email below to join Network to Code on Slack!&#x27;</p>

<p>https://networktocode.com/company/our-journey/ — Official NTC timeline: 2016 &#x27;Created the industry&#x27;s first Slack community for network automation&#x27;; 2018 &#x27;Slack community surpasses 10,000 members&#x27;; 2026 &#x27;Slack community surpasses 35,000 members&#x27;.</p>

<p>https://x.com/networktocode/status/1466135388817432584 — An NTC post (about 2021, seen via search result) announced &#x27;Network to Code&#x27;s public Slack hit 20,000 members!&#x27;</p>

<p>https://networktocode.com/community/ — NTC community page: &#x27;Join our Slack channel for all things related to network automation and Nautobot&#x27;, linking slack.networktocode.com.</p>

<p>Caveats: Direct curl of networktocode.com returned 403. The timeline and community pages were read through a fetch tool and search results.; Did not join the workspace, so the current channel list (e.g. whether an NSoT channel still exists) was not checked. Removing NSoT is editorial, not a confirmed error.; Could use the official site&#x27;s https URL. The http link currently redirects correctly.</p>

<p>Independent source check: Over 17,000 remains mathematically true when membership exceeds 35,000. Removing NSoT is explicitly admitted by the model to be editorial, with no channel inspection. HTTPS redirect cleanup is optional. This is not a supported necessary freshness correction; do not advertise it or accept the compound edit.</p>

<p>https://networktocode.com/company/our-journey/ — Official site reports more than 35,000 community members; this does not contradict the catalog lower bound.</p>

</details>

<h3>Puppet Community — keep</h3>

<p>Source or watched-source coverage changed since research.</p>

<details>
<summary>Evidence and limitations</summary>

<p>puppet.com/community redirects to the official https://www.puppet.com/community (&#x27;Join the Puppet Community | Perforce Puppet&#x27;). It still collects Puppet community resources: the Forge, community guidelines, Code of Conduct, event sponsorship, and Puppet Core free licensing. The description fits.</p>

<p>https://www.puppet.com/community — Official Perforce Puppet community page with FAQs on the Forge (modules, PDK, Bolt), Puppet Core free tier (up to 25 nodes), event sponsorship, Community Guidelines and Code of Conduct.</p>

<p>Caveats: The canonical host is now www.puppet.com/community. The current URL redirects fine, so a change is optional.; The community fork (OpenVox) after Perforce&#x27;s 2025 distribution changes is outside the scope of this official-resources entry.; &#x27;offical&#x27; typo is cosmetic.</p>

</details>

<h3>Salt Networks — keep</h3>

<p>Source or catalog stability was not confirmed for this review.</p>

<details>
<summary>Evidence and limitations</summary>

<p>The Google Group is reachable, and its welcome text still matches the description (&#x27;a central place to communicate goals about network device automation with SaltStack&#x27;). It is network-automation specific (e.g. posts by Mircea Ulinic on Salt network tooling). Activity is historic: the latest visible thread is 6/20/2019. Low activity is not grounds for removal, and the archive keeps reference value.</p>

<p>https://groups.google.com/g/salt-networks — &#x27;Welcome! The goal of this group is to have a central place to communicate goals about network device automation with SaltStack.&#x27; 5 threads; first meeting 2017-08-09; newest thread 6/20/19 (Mircea Ulinic, new salt-ssh-like CLI tool).</p>

<p>https://saltproject.io/community/working-groups/ — The current official working groups list (MacOS, Salt Extensions, Salt Formulas, Security, Windows) has no network working group. No documented successor.</p>

<p>Caveats: The group&#x27;s embedded Slack invite (saltstackcommunity.herokuapp.com) is dead because Salt moved to Discord. This does not affect the entry&#x27;s own link.; The maintainer may want to note that the group is historic/inactive. That is optional.</p>

<p>Independent source check: Independently fetched Google Group welcome text states the network-device-automation purpose and retains historic technical discussions. Age/absence from a newer group directory does not establish loss of relevance. Keep is defensible with historic-activity caveat.</p>

<p>https://groups.google.com/g/salt-networks — Reachable archive; welcome text describes central discussion of SaltStack network-device automation; technical posts visible.</p>

</details>

<h3>Salt Users — keep</h3>

<p>Source or catalog stability was not confirmed for this review.</p>

<details>
<summary>Evidence and limitations</summary>

<p>The salt-users Google Group is reachable, active, and used officially. Salt Project maintainer Shane Lee posted release announcements there in Sep and Oct 2026 (3006.30 LTS, 3007.17 STS, 3008.5 LTS). The welcome text calls it the Salt Users mailing list. The description &#x27;official forum of the Salt community&#x27; is broadly supported.</p>

<p>https://groups.google.com/g/salt-users — &#x27;Welcome to the Salt Users mailing list!&#x27; 8562 threads; latest posts Oct 26 and Oct 23 2026 announce Salt Project releases 3006.30/3007.17/3008.5.</p>

<p>https://saltproject.io/community/ — The main Salt Project community links are now Discord, GitHub, event calendar and working groups. The Google Group is not prominently linked there, so &#x27;the official forum&#x27; is arguably less exclusive than before.</p>

<p>Caveats: The primary real-time community is now Discord. &#x27;Official forum&#x27; remains defensible because official release announcements are still posted to the group.</p>

</details>

<h3>Ansible NYC Meetup — keep</h3>

<p>Source or watched-source coverage changed since research.</p>

<details>
<summary>Evidence and limitations</summary>

<p>The Meetup group is live: &#x27;Ansible NYC&#x27;, New York, 725 members, a group of systems engineers and DevOps folks meeting to talk about Ansible. The description &#x27;Local NYC Ansible user meetup&#x27; is accurate. The most recent listed event was in November 2020. Low activity alone is not a reason to remove.</p>

<p>https://www.meetup.com/ansible-nyc/ — Group &#x27;Ansible NYC&#x27;, New York, NY, 725 members, 24 past events. Latest listed: &#x27;Ansiblefest Round Up and QA with Tim Appnel&#x27;, Nov 10, 2020 (online). Earlier events include &#x27;Multicloud Networking Leveraging Ansible and Pureport&#x27;.</p>

<p>Caveats: No upcoming events were visible. The group seems dormant since 2020, but the page and archive remain.</p>

</details>

<h3>NANOG — keep</h3>

<p>Source snapshot unavailable.</p>

<details>
<summary>Evidence and limitations</summary>

<p>NANOG is an active network operators&#x27; community with regular automation content. In 2026 its programme included &#x27;The Network Automation Map: Navigate Your Journey with the NAF Automation Framework&#x27; and a network automation panel at NANOG 96 (Feb 2026), a Network Automation BoF at NANOG 97 (June 2026), and a keynote on autonomous networks at NANOG 98 (Oct 2026). The description &#x27;with fair share of automation presentations/discussions&#x27; is supported. www.nanog.org is behind a Cloudflare JS challenge (403 to scripts), which is an access limitation, not a dead site.</p>

<p>https://nanog.org/events/nanog-97/content/5732/ — Seen via search result: &#x27;Network Automation BoF&#x27; at NANOG 97 (Bellevue, June 1, 2026), led by Ryan Hamel (Zayo). Direct fetch returned the Cloudflare challenge (403).</p>

<p>https://nanog.org/events/nanog-96/content/5625/ — Seen via search result: NANOG 96 talk &#x27;The Network Automation Map: Navigate Your Journey with the NAF Automation Framework&#x27; (Damien Garros, Wim Henderickx), Feb 2, 2026.</p>

<p>https://lists.nanog.org/archives/list/nanog-announce@lists.nanog.org/2026/4/ — The official NANOG list archive is reachable (HTTP 200), with monthly nanog-announce archives through November 2026. This shows the organization is active.</p>

<p>Caveats: www.nanog.org returned 403 (Cloudflare &#x27;Just a moment…&#x27;) to curl and 402 to the fetch tool. The homepage was not read directly, so a recheck is warranted. Session details come from search-indexed nanog.org pages.</p>

<p>Source snapshot incomplete; excluded from the saved baseline.</p>

</details>

<h3>Tech Field Day — keep</h3>

<p>Source or watched-source coverage changed since research.</p>

<details>
<summary>Evidence and limitations</summary>

<p>The site is live and its own description matches the entry: an invite-only technical meeting where sponsoring enterprise IT companies present to independent delegates through presentations, demos and roundtables. It is now a Futurum Group company. It still runs a Networking Field Day track and has 2026 sponsor and delegate lists, so it remains relevant for vendor network and automation presentations.</p>

<p>https://techfieldday.com/ — The og:description says &#x27;Tech Field Day, a Futurum Group company, is an invite-only technical meeting between delegates from around the world and sponsoring enterprise IT companies that share their products and ideas through presentations, demos, roundtables&#x27;. The navigation includes &#x27;Networking Field Day&#x27; and 2026 sponsors and delegates.</p>

<p>Caveats: Tech Field Day covers enterprise IT broadly. Its network automation fit comes mainly through Networking Field Day content, so fit is a maintainer judgement.</p>

</details>

<h3>Python for Network Engineers — keep</h3>

<p>Source or catalog stability was not confirmed for this review.</p>

<details>
<summary>Evidence and limitations</summary>

<p>Kirk Byers&#x27; Python Network Automation course page is live. It shows current packages and a syllabus covering Git, Netmiko, TextFSM, YAML/JSON and CiscoConfParse, and advertises a free course starting November 12. This matches the network automation description.</p>

<p>https://pynet.twb-tech.com/class.html — The title is &#x27;Python for Network Engineers - Python Network Automation Course&#x27;. The page lists Starter, Plus and Premium packages, a syllabus (Netmiko, TextFSM, YAML/JSON, CiscoConfParse and more) and &#x27;Free Course Starts November 12&#x27;.</p>

<p>Caveats: Some package options (lab environment, forum) are shown as &#x27;NOT AVAILABLE&#x27;, which does not affect the description.</p>

</details>

<h3>Eric Chou - PythonicNetneg — keep</h3>

<p>Source or watched-source coverage changed since research.</p>

<details>
<summary>Evidence and limitations</summary>

<p>The blog is live as &#x27;Network Automation Nerds&#x27; by Eric Chou, &#x27;formerly Python for Network Engineers&#x27;. Its last post is from May 2020 and points readers to networkautomation.ninja. It remains a historic network automation blog by the stated author.</p>

<p>https://blog.pythonicneteng.com/ — The title is &#x27;Network Automation Nerds&#x27; with the og:description &#x27;Tools for the Network Warriors (formerly Python for Network Engineers)&#x27;. The latest post (26 May 2020) by Eric Chou links to networkautomation.ninja.</p>

<p>Caveats: Eric Chou&#x27;s later blogging appears to have moved to networkautomation.ninja. I did not verify that site, so no URL change is proposed.; The entry name contains the typo &#x27;PythonicNetneg&#x27;. This is cosmetic, and the site title is now &#x27;Network Automation Nerds&#x27;.</p>

</details>

<h3>Mircea Ulinic — keep</h3>

<p>Source or catalog stability was not confirmed for this review.</p>

<details>
<summary>Evidence and limitations</summary>

<p>Mircea Ulinic&#x27;s blog is active and its tagline is &#x27;Network automation, infrastructure and distributed systems&#x27;, so the network automation fit is confirmed. The informal description makes a hedged &#x27;may include&#x27; claim that is still compatible with the site.</p>

<p>https://mirceaulinic.net/ — Returns HTTP 200 with the tagline &#x27;Network automation, infrastructure and distributed systems.&#x27; A recent post, &#x27;Ten years later, I finally updated the blog&#x27;, says the site moved from Jekyll/GitHub Pages to Hugo/Cloudflare. Dates on the page run up to 2026-09-20.</p>

<p>Caveats: The tongue-in-cheek wording (&#x27;vendor bashing or machine learning (TBD)&#x27;) could optionally be modernised, but it is not factually false.</p>

</details>

<h3>OpsMill Blog — keep</h3>

<p>Source or catalog stability was not confirmed for this review.</p>

<details>
<summary>Evidence and limitations</summary>

<p>The OpsMill blog is active and its self-description exactly matches the listed description. Its posts cover network and infrastructure automation (Infrahub, Nornir/NAPALM/Netmiko/Scrapli, brownfield network automation). It is a vendor blog that serves a network automation need.</p>

<p>https://opsmill.com/blog/ — The blog describes itself as &#x27;Business strategy &amp; technical deep dives for powering infrastructure automation.&#x27; Recent posts include &#x27;Infrahub 1.12 Strengthens Automation Change Management...&#x27; (Nov 10, 2026) and &#x27;How Nornir, NAPALM, Netmiko, and Scrapli Work Together&#x27; (Oct 19, 2026).</p>

<p>Caveats: Direct curl requests got a Cloudflare/WP Engine 403. The content was read through an alternate fetcher.</p>

</details>

<h3>Python for Network Engineers — keep</h3>

<p>Source or catalog stability was not confirmed for this review.</p>

<details>
<summary>Evidence and limitations</summary>

<p>Kirk Byers&#x27; Python for Network Engineers articles page is reachable and still has Netmiko and NETCONF articles. The description says &#x27;Netmiko, NAPALM, and Ansible&#x27; without claiming those are the only topics, so it remains supported.</p>

<p>https://pynet.twb-tech.com/blog/ — Returns HTTP 200 with the title &#x27;Python for Network Engineers - Articles &amp; Videos&#x27;. Recent articles include &#x27;NETCONF: Abstract the Abstraction&#x27;, &#x27;IOS-XE and NETCONF Candidate Configuration Testing&#x27;, and &#x27;Netmiko4: ConnLogOnly&#x27;.</p>

<p>Caveats: I did not check whether the NAPALM and Ansible articles are still in the archive. Only recent articles were seen.</p>

</details>

<h3>Open-Source Routing and Network Simulation - Brian Linkletter — keep</h3>

<p>Source snapshot unavailable.</p>

<details>
<summary>Evidence and limitations</summary>

<p>Brian Linkletter&#x27;s blog is reachable and still covers open-source network emulation and simulation tools, with posts in 2026 (Containerlab, Kathará, Cloonix). This matches the description.</p>

<p>https://www.brianlinkletter.com/ — The blog title is &#x27;Open-Source Routing and Network Simulation&#x27;. Recent posts include &#x27;Building IRRd and bgpq4 Docker Containers for Network Labs&#x27; (Mar 22, 2026), &#x27;Containerlab Network Emulator v0.73 Review&#x27; (Mar 3, 2026) and &#x27;Open-source network simulators and emulators in 2026&#x27;.</p>

<p>Caveats: Direct curl got a Cloudflare JS challenge (403). The content was read through an alternate fetcher.; The fit is on the network-emulation side of network automation (lab tooling such as Containerlab), which is consistent with how it was originally listed.</p>

<p>Source snapshot incomplete; excluded from the saved baseline.</p>

</details>

<h3>JSON Viewer Tool — keep</h3>

<p>Source or catalog stability was not confirmed for this review.</p>

<details>
<summary>Evidence and limitations</summary>

<p>The page loads, and every claim in the description is confirmed by the page itself: it is free, conversion runs client-side, and output options include indent, quoting and null style.</p>

<p>https://jsonviewertool.com/json-to-yaml — The UI has &#x27;Indent spaces&#x27;, &#x27;Line width&#x27;, &#x27;Sort keys&#x27;, &#x27;Force quotes&#x27;, &#x27;Quote style (Double/Single)&#x27; and &#x27;Null style (null / ~ / empty)&#x27;. The page&#x27;s structured data says &#x27;Convert JSON to YAML locally in your browser&#x27; and &#x27;The converter is 100% client-side JavaScript: no signup, no upload&#x27;, and lists price 0.</p>

<p>Caveats: I did not run a conversion or confirm that no data is uploaded. The client-side claim comes from the site&#x27;s own text.; Network-automation fit is the same as the other generic JSON/YAML utilities in this section.</p>

</details>

<h3>XML to JSON converter online — keep</h3>

<p>Source or catalog stability was not confirmed for this review.</p>

<details>
<summary>Evidence and limitations</summary>

<p>The http URL redirects to the https version of the same page. The tool still converts XML to JSON, and the site has a companion JSON-to-XML page, so the description holds.</p>

<p>https://www.utilities-online.info/xmltojson/ — The page is titled &#x27;XML to JSON &amp; JSON to XML converter online&#x27; and has XML and JSON panes with a Convert button.</p>

<p>https://www.utilities-online.info/jsontoxml — The separate JSON-to-XML converter page returns HTTP 200.</p>

<p>Caveats: The listed URL is http and redirects to https. Switching to https is optional housekeeping, not a factual correction.; I did not run a conversion.</p>

</details>

<h3>Python at Codecademy — keep</h3>

<p>Source or catalog stability was not confirmed for this review.</p>

<details>
<summary>Evidence and limitations</summary>

<p>The Codecademy Learn Python 3 course page loads and still offers a Python course, which matches &#x27;Learn Python by Codecademy&#x27;.</p>

<p>https://www.codecademy.com/learn/learn-python-3 — The page is titled &#x27;Learn Python 3 | Codecademy&#x27; and reads &#x27;Learn the basics of Python 3.13&#x27;. It lists projects, quizzes and a certificate.</p>

<p>Caveats: I did not check which parts of the course are free and which need a paid plan.</p>

</details>

<h3>Real Python — keep</h3>

<p>Source or catalog stability was not confirmed for this review.</p>

<details>
<summary>Evidence and limitations</summary>

<p>Real Python is live and still publishes tutorials, video courses, books, learning paths and a podcast, with recent content dated November 2026. The description holds up, and general Python learning fits the Python section. www.realpython.com returns 403 to non-browser clients, and the snapshot shows https://realpython.com/ as the canonical host. That is optional URL cleanup, not a factual error.</p>

<p>https://realpython.com/ — Title &#x27;Real Python: Build Real-World Python Skills&#x27;. Meta description mentions expert-written tutorials, video courses and quizzes. Links to /books/, /courses/, /learning-paths/ and /podcasts/rpp/. Latest dates on page: 2026-11-06.</p>

<p>https://realpython.com/products/books/ — Page &#x27;Python Books by Real Python&#x27; is live (HTTP 200), so the books claim holds.</p>

<p>Caveats: www.realpython.com returned 403 to curl (likely bot filtering). Recheck rather than treat as a failure. The apex domain is optional cleanup.</p>

</details>

<h3>Cisco IOS XE CSR1000V — keep</h3>

<p>Source snapshot unavailable.</p>

<details>
<summary>Evidence and limitations</summary>

<p>The Cisco guide is reachable via WebFetch (curl got 403, likely bot filtering). Its title is &#x27;Cisco IOS XE REST API Management Reference Guide&#x27; for the CSR 1000V (with ASR 1000 support), matching the description exactly. The product line is legacy, but this is a historic vendor API reference and the description makes no claim of being current.</p>

<p>https://www.cisco.com/c/en/us/td/docs/routers/csr1000/software/restapi/restapi/RESTAPIintro.html — Title &#x27;Cisco IOS XE REST API Management Reference Guide&#x27;, Cisco Cloud Services Router 1000V Series. REST APIs are &#x27;an alternative method to the Cisco IOS XE CLI for provisioning selected functions&#x27;. No deprecation notice in the intro chapter.</p>

<p>Caveats: Direct curl returned HTTP 403, while WebFetch succeeded. Cisco.com may block automated fetches, so recheck rather than remove.; The CSR 1000V was succeeded by the Catalyst 8000V, but I did not find an official statement on this specific REST API&#x27;s status, so I did not infer one.</p>

<p>Source snapshot incomplete; excluded from the saved baseline.</p>

</details>

<h3>Cisco IOS-XR — keep</h3>

<p>Source snapshot unavailable.</p>

<details>
<summary>Evidence and limitations</summary>

<p>The link resolves to the official &#x27;Cisco IOS XR XML API Guide, Cisco IOS XR Release 4.1&#x27; (last updated 2011). It is historic vendor API documentation, and &#x27;Cisco IOS-XR API Docs only&#x27; is not false.</p>

<p>https://www.cisco.com/c/en/us/td/docs/ios_xr_sw/iosxr_r4-1/xml/programming/guide/xl41apidoc.html — Title &#x27;Cisco IOS XR XML API Guide, Cisco IOS XR Release 4.1&#x27;. Documents the XML API (configuration management, operational requests, security). Last updated March 29, 2011.</p>

<p>Caveats: Optional clarification: the description could name it as the XR 4.1 XML API guide so readers know it is historic. This is not a factual correction.; Direct curl got HTTP 403; content was read via WebFetch. The current support status of the XR XML API in later releases was not researched.</p>

<p>Source snapshot incomplete; excluded from the saved baseline.</p>

</details>

<h3>Getting Started with the ios_config Ansible Module — keep</h3>

<p>Source or catalog stability was not confirmed for this review.</p>

<details>
<summary>Evidence and limitations</summary>

<p>The YouTube video is live. oEmbed metadata confirms the title and author (Jason Edelman), and it was published 2017-04-25. The ios_config module it introduces still exists as cisco.ios.ios_config in current Ansible docs. This is a dated tutorial that is still relevant, and age is not a removal reason.</p>

<p>https://www.youtube.com/oembed?url=https://www.youtube.com/watch?v=WXLUgDmvHDI&amp;format=json — title &#x27;Getting Started with the ios_config Ansible Module&#x27;, author_name &#x27;Jason Edelman&#x27; (@jedelman23).</p>

<p>https://www.youtube.com/watch?v=WXLUgDmvHDI — publishDate 2017-04-25. Description: &#x27;In under 30 minutes, get familiar with the Ansible ios_config module and how to specifically send global configuration commands to one or more network device...&#x27;</p>

<p>https://docs.ansible.com/ansible/latest/collections/cisco/ios/ios_config_module.html — Resolves (200) to the current cisco.ios.ios_config module documentation.</p>

<p>Caveats: The &#x27;of NetworkToCode&#x27; affiliation comes from the existing entry and was not separately confirmed from the video page. Edelman founded Network to Code.; The video predates Ansible collections, so module naming and syntax may differ from current releases.</p>

</details>

<h3>Arista Network Test Automation — keep</h3>

<p>Source or watched-source coverage changed since research.</p>

<details>
<summary>Evidence and limitations</summary>

<p>The ANTA stable docs are live, and the home page states verbatim &#x27;ANTA is a Python framework that automates tests for Arista devices.&#x27; The name &#x27;Arista Network Test Automation&#x27; matches the page title. Network state validation (NRFU and similar) is a clear automation fit.</p>

<p>https://anta.arista.com/stable/ — Title &#x27;Home - Arista Network Test Automation - ANTA&#x27;. Heading &#x27;Arista Network Test Automation (ANTA) Framework&#x27;. Text: &#x27;ANTA is a Python framework that automates tests for Arista devices. ANTA provides a set of tests to validate the state of your network... Automate NRFU (Network Ready For Use) tests&#x27;. The page references v1.10.0.</p>

</details>

<h3>Video — keep</h3>

<p>Source or catalog stability was not confirmed for this review.</p>

<details>
<summary>Evidence and limitations</summary>

<p>The YouTube playlist &#x27;Getting to know Batfish&#x27; is live. It is published by the Batfish channel (@Intentionet), contains 8 videos and was last updated May 24, 2019. The pybatfish notebook README links videos from it, such as Ca7kPAtfFqo. These are dated but still relevant tutorials.</p>

<p>https://www.youtube.com/oembed?url=https://www.youtube.com/playlist?list=PLUXUN_5CNTWJeMUqbUFcdi2qPnm_2mit3&amp;format=json — title &#x27;Getting to know Batfish&#x27;, author_name &#x27;Batfish&#x27; (/@Intentionet), first video Ca7kPAtfFqo.</p>

<p>https://www.youtube.com/playlist?list=PLUXUN_5CNTWJeMUqbUFcdi2qPnm_2mit3 — numVideosText &#x27;8&#x27;. &#x27;Last updated on May 24, 2019&#x27;. Video durations of 4–12 minutes.</p>

<p>https://raw.githubusercontent.com/batfish/pybatfish/master/jupyter_notebooks/README.md — &#x27;Getting Started with Batfish&#x27; notebook links video https://www.youtube.com/watch?v=Ca7kPAtfFqo, the first video in the playlist.</p>

<p>Caveats: The videos date from 2019, so the UI and API shown may differ from current pybatfish.</p>

</details>

<h3>Using Chef Client with Cisco NX-OS — keep</h3>

<p>Source snapshot unavailable.</p>

<details>
<summary>Evidence and limitations</summary>

<p>The Cisco page returns 403 to curl, which is bot blocking, but WebFetch read it successfully. It is the &#x27;Using Chef Client with Cisco NX-OS&#x27; chapter of the Nexus 9000 NX-OS Programmability Guide, Release 7.x. It covers Chef concepts, prerequisites and cisco-cookbook. The title and description are accurate, and Chef-based switch configuration is network automation. Cisco still ships the same chapter in 10.x guides (10.1, 10.3, 10.6), so the topic is not obsolete. The 7.x page is a dated but valid resource.</p>

<p>https://www.cisco.com/c/en/us/td/docs/switches/datacenter/nexus9000/sw/7-x/programmability/guide/b_Cisco_Nexus_9000_Series_NX-OS_Programmability_Guide_7x/b_Cisco_Nexus_9000_Series_NX-OS_Programmability_Guide_7x_chapter_01110.html — Title &#x27;Cisco Nexus 9000 Series NX-OS Programmability Guide, Release 7.x - Using Chef Client with Cisco NX-OS&#x27;. Covers Chef cookbooks and recipes, prerequisites and cisco-cookbook. Notes that from NX-OS 9.2(1) a bash-shell install of chef-client is unsupported and Guest Shell must be used.</p>

<p>https://www.cisco.com/c/en/us/td/docs/dcn/nx-os/nexus9000/103x/programmability/cisco-nexus-9000-series-nx-os-programmability-guide-release-103x/m-n9k-using-chef-client-with-cisco-nx-os-101x.html — Search shows the same chapter in the NX-OS 10.3(x) Programmability Guide, with 10.1(x) and 10.6(x) versions as well. I did not open these pages directly.</p>

<p>Caveats: Plain HTTP clients get 403 from cisco.com, which is likely bot protection. Link checkers may need an exception, and a recheck is warranted rather than removal.; Maintainers could optionally point to a newer 10.x chapter, but the 7.x page is still accurate for its release. I did not verify the current status of the cisco-cookbook on Chef Supermarket.</p>

<p>Source snapshot incomplete; excluded from the saved baseline.</p>

</details>

<h3>Clixon Home Page — keep</h3>

<p>Source or catalog stability was not confirmed for this review.</p>

<details>
<summary>Evidence and limitations</summary>

<p>clicon.org is live (HTTP 200, title &#x27;Clixon project&#x27;). It describes the Clixon, Clixon controller and CLIgen projects and links to each one&#x27;s GitHub repository and readthedocs user guide, which matches the entry. Clixon is presented as tooling for automated configuration management and network automation.</p>

<p>https://clicon.org — Title &#x27;Clixon project&#x27;. Text: &#x27;The Clixon open-source project provides tools for automated configuration management include: Clixon for YANG-based devices, Clixon controller for network automation, CLIgen...&#x27;. Links to github.com/clicon/clixon, clixon-controller, cligen, clixon-examples, clixon-pyapi, clixon-docs.readthedocs.io and clixon-controller-docs.readthedocs.io.</p>

<p>Caveats: The page&#x27;s licence wording (&#x27;GPLv3 or Apache2&#x27;) differs from the repository README (&#x27;Apache 2.0 or GPLv2&#x27;). The entry makes no licence claim, so this does not affect it.</p>

</details>

<h3>Salt RIPE-74 — keep</h3>

<p>Source snapshot unavailable.</p>

<details>
<summary>Evidence and limitations</summary>

<p>The PDF is reachable (HTTP 200, application/pdf, 88 pages). It is Mircea Ulinic&#x27;s RIPE 74 talk (Cloudflare, Budapest, May 2017), &#x27;Network automation at scale – Up and running in 60 minutes&#x27;, covering SaltStack configuration and network configuration management. Its advanced topics include beacons and event-tag-driven automatic router config updates, which supports the &#x27;event-driven&#x27; wording. It is a historic presentation and still relevant.</p>

<p>https://ripe74.ripe.net/presentations/18-RIPE-74-Network-automation-at-scale-up-and-running-in-60-minutes.pdf — Slide 1: &#x27;Network automation at scale – Up and running in 60 minutes&#x27;, Mircea Ulinic, Cloudflare, RIPE 74 Budapest, May 2017. Agenda: Meet the tools, Install, Configure SaltStack, CLI syntax, Configuration management, Advanced topics. Slide 70: &#x27;Beacon event tag example... whenever you update /etc/salt/pillar/ntp_config.sls, it will automatically update your routers&#x27; config.&#x27;</p>

<p>Caveats: The snapshot&#x27;s failure was a ValueError (probably PDF handling), not unreachability; a direct fetch succeeded.; Many links inside the slides point to docs.saltstack.com URLs that no longer resolve. This is expected for a dated presentation.</p>

<p>Source snapshot incomplete; excluded from the saved baseline.</p>

</details>

<h3>StackStorm Youtube — keep</h3>

<p>Source or catalog stability was not confirmed for this review.</p>

<details>
<summary>Evidence and limitations</summary>

<p>The channel resolves without a redirect and is titled &quot;StackStorm&quot;. Its RSS feed lists official StackStorm tutorial videos (Actions, Rules, Workflows, StackStorm Exchange, Advanced Actions). The description, &quot;intro, marketing, interviews, technical product talks&quot;, is a fair, non-exclusive summary. Because the content is historic training material, it can stay even if the channel is quiet.</p>

<p>https://www.youtube.com/channel/UCColc5CuBJ8-1SnALnkDz8Q — HTTP 200 with no redirect. og:title is &quot;StackStorm&quot; and the meta description reads &quot;StackStorm is an emerging leader of the third wave of operations automation...&quot;.</p>

<p>https://www.youtube.com/feeds/videos.xml?channel_id=UCColc5CuBJ8-1SnALnkDz8Q — The feed lists videos titled &quot;Actions - StackStorm Tutorials&quot;, &quot;Rules - StackStorm Tutorials&quot;, &quot;Workflows - StackStorm Tutorials&quot;, &quot;StackStorm Exchange - StackStorm Tutorials&quot; and &quot;Advanced Actions - StackStorm Tutorials&quot;, all published 2019-03-13 in the feed.</p>

<p>Caveats: Only the RSS feed&#x27;s most recent entries were checked, not the full video catalog, so the marketing and interview videos were not individually confirmed.</p>

</details>

<h3>SuzieQ Youtube — keep</h3>

<p>Source or catalog stability was not confirmed for this review.</p>

<details>
<summary>Evidence and limitations</summary>

<p>The handle resolves to the &quot;Suzieq Project&quot; channel. Its description says the channel is focused on the SuzieQ open-source network observability platform. The feed shows community meetups (Oct 2022 to Apr 2023) and a Getting Started demo, which matches the description. As a historic community and training resource it remains relevant despite no recent uploads in the feed.</p>

<p>https://www.youtube.com/@suzieqproject7168 — HTTP 200. og:title is &quot;Suzieq Project&quot; and the description reads &quot;This channel is focused on the Suzieq open source multi-vendor network observability platform...&quot;.</p>

<p>https://www.youtube.com/feeds/videos.xml?channel_id=UC2QKM4DqDbEQMMpU9GQUpdA — Recent entries are &quot;SuzieQ April Community Meetup&quot; (2023-04-13), &quot;SuzieQ March Community Meetup&quot; (2023-03-09), &quot;SuzieQ Community Meetup: Dec 2022&quot;, &quot;SuzieQ October Community Meetup&quot; (2022-10-13) and &quot;Suzieq Getting Started&quot; (2021-04-09).</p>

<p>Caveats: The newest feed entry is from April 2023, so this is historic content. I did not confirm from the SuzieQ repository that the channel is official; the evidence is the channel&#x27;s own name and description.</p>

</details>

<h3>NUTS — keep</h3>

<p>Source snapshot unavailable.</p>

<details>
<summary>Evidence and limitations</summary>

<p>The packet snapshot failed, but https://github.com/network-unit-testing-system loads (HTTP 200) and contains the nuts repo. The nuts README and pyproject (v3.6.0) confirm a custom pytest plugin, registered through the pytest11 entry point, that runs network tests via Nornir from YAML test bundles. The description is accurate.</p>

<p>https://github.com/network-unit-testing-system — HTTP 200. The org lists the nuts, nuts-containerlab-demo, naf_workshop_nuts, nuts-oc-tests and nuts-client-tests repos.</p>

<p>https://raw.githubusercontent.com/network-unit-testing-system/nuts/HEAD/README.md — &#x27;Nuts itself is written as a custom pytest plugin. In the background, nornir executes specific network tasks&#x27;. &#x27;Currently only yaml files are supported as test bundles&#x27;.</p>

<p>https://raw.githubusercontent.com/network-unit-testing-system/nuts/HEAD/pyproject.toml — name nuts, version 3.6.0, description &#x27;Network Unit Testing System&#x27;, pytest&gt;=9.0, [project.entry-points.pytest11].</p>

<p>Caveats: The entry links to the GitHub organization, not the nuts repo. Pointing it at https://github.com/network-unit-testing-system/nuts is optional, not a correction.; The automated snapshot failure looks like a fetch-tool problem. The URL was reachable when checked manually.</p>

<p>Source snapshot incomplete; excluded from the saved baseline.</p>

</details>

<h3>InfluxDB — keep</h3>

<p>Source or catalog stability was not confirmed for this review.</p>

<details>
<summary>Evidence and limitations</summary>

<p>www.influxdata.com returns 200 and still presents InfluxDB as a time-series database and platform aimed at developers (&#x27;Time series starts with InfluxDB&#x27;, &#x27;Developers choose InfluxDB&#x27;). The entry&#x27;s marketing-style claim is still supported, and time-series storage is a common part of network telemetry stacks.</p>

<p>https://www.influxdata.com/ — Returns 200. Site schema description is &#x27;The Platform for Time-Series Data&#x27;. Page text includes &#x27;Time series starts with InfluxDB&#x27;, &#x27;Developers choose InfluxDB&#x27;, &#x27;Time series database&#x27; and &#x27;Performance and scale for complex time series workloads&#x27;.</p>

<p>Caveats: The URL is the company homepage, not a product page. A more specific page such as https://www.influxdata.com/products/influxdb/ was not checked; this is optional.; The description is volatile marketing copy, not an exact quote of current text.</p>

</details>

<h3>Telegraf — keep</h3>

<p>Source or catalog stability was not confirmed for this review.</p>

<details>
<summary>Evidence and limitations</summary>

<p>The Telegraf page returns 200 without redirect. It describes Telegraf as an open-source server agent for collecting metrics, logs and data, with 400+ plugins. The entry&#x27;s claim is still supported.</p>

<p>https://www.influxdata.com/time-series-platform/telegraf/ — Returns 200 with no redirect. Meta description: &#x27;Telegraf is an open source server agent that makes it easy to collect metrics, logs, and data.&#x27; Body: &#x27;Open source agent for collecting metrics from infrastructure, applications, and devices. Use 400+ community-tested plugins…&#x27;</p>

<p>Caveats: Network-specific inputs such as SNMP and gNMI were not verified on this page. The listed description does not claim them.</p>

</details>

<h3>Grafana — keep</h3>

<p>Source or watched-source coverage changed since research.</p>

<details>
<summary>Evidence and limitations</summary>

<p>grafana.com returns 200. Grafana is still Grafana Labs&#x27; open-source observability and visualization product, so &#x27;An open source observability platform&#x27; is still accurate. The homepage now leads with Grafana Cloud, but the open-source product is still offered.</p>

<p>https://grafana.com/ — Returns 200. Title &#x27;Full-stack observability for the agentic era | Grafana Labs&#x27;. The page promotes Grafana Cloud, and its navigation includes an Open Source section and downloads.</p>

<p>https://grafana.com/oss/grafana/ — Grafana Labs&#x27; open-source Grafana product page is reachable. The site states &#x27;Open source is at the heart of what we do at Grafana Labs.&#x27;</p>

<p>Caveats: The root URL now leads with the commercial Grafana Cloud offering. The maintainer may optionally point to https://grafana.com/oss/grafana/, but this is not a factual correction.</p>

</details>

<h3>J2Live - TTL255 — keep</h3>

<p>Source snapshot unavailable.</p>

<details>
<summary>Evidence and limitations</summary>

<p>The service is still up; the failure is TLS only. The Let&#x27;s Encrypt certificate for j2live.ttl255.com expired on 2026-11-08, two days before this check, so normal HTTPS clients fail. Fetching with verification disabled returns the live &#x27;TTL255 J2Live - Live Jinja2 Parser&#x27; page, with Ansible and Salt engine options. The description is accurate. Recheck later; do not remove.</p>

<p>https://j2live.ttl255.com/ — curl fails verification: certificate subject CN=j2live.ttl255.com, issuer Let&#x27;s Encrypt, expire date Nov 8 2026 GMT. Plain HTTP redirects to HTTPS.</p>

<p>https://j2live.ttl255.com/ — With verification disabled the page loads. Title &#x27;TTL255 J2Live - Live Jinja2 Parser&#x27;. Text: &#x27;Online Jinja2 Parser and Renderer by TTL255&#x27;. Engine options include &#x27;Ansible - base J2 engine with Ansible filters&#x27; and &#x27;Salt - enhanced Salt Jinja2 engine&#x27;.</p>

<p>Caveats: The certificate expired very recently. This is likely a lapsed renewal, but it is unknown whether the owner will renew it. Recheck before any further action.; The page was read with certificate verification disabled, for observation only.</p>

<p>Source snapshot incomplete; excluded from the saved baseline.</p>

</details>

<h3>KVM — keep</h3>

<p>Source or catalog stability was not confirmed for this review.</p>

<details>
<summary>Evidence and limitations</summary>

<p>The official KVM wiki still describes KVM as a full virtualization solution for Linux, with the kernel component in mainline Linux. The description is accurate apart from a typo (&quot;build&quot; for &quot;built&quot;).</p>

<p>https://www.linux-kvm.org/page/Main_Page — &quot;KVM (for Kernel-based Virtual Machine) is a full virtualization solution for Linux on x86 hardware containing virtualization extensions (Intel VT or AMD-V)... The kernel component of KVM is included in mainline Linux, as of 2.6.20.&quot;</p>

<p>Caveats: The description has a minor typo (&quot;build&quot; should be &quot;built&quot;). This is cosmetic, not a factual error.</p>

</details>

<h3>Proxmox — keep</h3>

<p>Source or catalog stability was not confirmed for this review.</p>

<details>
<summary>Evidence and limitations</summary>

<p>The official overview confirms Proxmox VE is open source, integrates KVM and LXC, and has a web interface. The listed URL works through a temporary (302) redirect to the products overview page.</p>

<p>https://www.proxmox.com/en/proxmox-ve — Returns HTTP 302 Moved Temporarily to https://www.proxmox.com/en/products/proxmox-virtual-environment/overview.</p>

<p>https://www.proxmox.com/en/products/proxmox-virtual-environment/overview — &quot;Proxmox Virtual Environment is a complete, open-source server management platform for enterprise virtualization. It tightly integrates the KVM hypervisor and Linux Containers (LXC), software-defined storage and networking functionality... With the integrated web-based user interface you can manage VMs and containers&quot;.</p>

<p>Caveats: The REST API claim was not re-read on this page. It is long-standing Proxmox VE functionality but is unverified in this pass.; Because the redirect is temporary (302), I did not propose a URL change.</p>

</details>

<h3>GNS3 — keep</h3>

<p>Source or catalog stability was not confirmed for this review.</p>

<details>
<summary>Evidence and limitations</summary>

<p>GNS3 is still &quot;GNS3 Graphical Network Simulator&quot; according to its official GitHub repository. The homepage and the 3.1 docs site are live.</p>

<p>https://www.gns3.com/ — Returns HTTP 200. Content is client-rendered (served an &#x27;Incompatible Browser&#x27; fallback to curl).</p>

<p>https://github.com/GNS3/gns3-gui — og:title &quot;GitHub - GNS3/gns3-gui: GNS3 Graphical Network Simulator&quot;. The README points to https://docs.gns3.com/.</p>

<p>https://docs.gns3.com/docs/ — The GNS3 Documentation site is live, with navigation for 3.1 Docs. Copyright 2026 GNS3 Technologies Inc.</p>

<p>Caveats: The homepage requires JavaScript, so I could not read its text.</p>

</details>

<h3>CML — keep</h3>

<p>Source snapshot unavailable.</p>

<details>
<summary>Evidence and limitations</summary>

<p>curl gets HTTP 403 (Akamai Access Denied), but WebFetch retrieved the same cisco.com page: titled Cisco Modeling Labs, it describes a network simulation platform with an HTML5 UI and comprehensive API. The DevNet CML site confirms the same and shows CML 2.10 with an MCP server. This looks like bot blocking, not a dead page. The description (emulator with both API and GUI) is supported. &quot;Replaces VIRL&quot; is a historical claim that stays valid.</p>

<p>https://www.cisco.com/c/en/us/products/cloud-systems-management/modeling-labs/index.html — curl returns HTTP 403 Access Denied (edgesuite). WebFetch retrieved the page: title &quot;Cisco Modeling Labs&quot;, &quot;our premier platform for network simulation&quot;, HTML5 user interface and comprehensive API, on-premises, Cisco or multi-vendor networks, tiers including free.</p>

<p>https://developer.cisco.com/modeling-labs/ — &quot;Cisco Modeling Labs is our premier platform for network simulation. With an easy-to-use HTML5 UI and a comprehensive API...&quot; Also: &quot;What&#x27;s new in CML 2.10: Integrate your preferred AI tool with CML&#x27;s MCP Server&quot;.</p>

<p>Caveats: The listed URL returns 403 to some automated clients, so link checks may need a recheck or exception. This is not grounds for removal.; The current pages do not mention VIRL. The replacement claim is historical and was not re-verified on them.</p>

<p>Source snapshot incomplete; excluded from the saved baseline.</p>

</details>

<h3>Device42 — keep</h3>

<p>Source or watched-source coverage changed since research.</p>

<details>
<summary>Evidence and limitations</summary>

<p>device42.com (now &#x27;A Freshworks Company&#x27;) still offers automated hybrid IT discovery, CMDB, dependency mapping, DCIM and IPAM. It has a documented REST API (OpenAPI 3.0) and integrations. The listed capabilities are supported.</p>

<p>https://www.device42.com/ — The page is titled &#x27;Device42, A Freshworks Company&#x27;. It advertises discovery, asset management and dependency mapping for data center and cloud.</p>

<p>https://www.device42.com/features/ip-address-management/ — The IPAM page lists IPv4/IPv6 management, auto-discovery, subnet trees, and &#x27;Powerful APIs enable IP search, find, and integration&#x27;.</p>

<p>https://www.device42.com/data-center-infrastructure-management/ — The DCIM page describes rack and room layouts and mapping &#x27;physical, virtual and cloud networks automatically and agentlessly&#x27;.</p>

<p>https://api.device42.com/ — The Device42 API Reference (OpenAPI 3.0) is live.</p>

<p>Caveats: I did not verify the &#x27;Mostly leverages SNMP or vendor provided APIs&#x27; or webhook claims in detail. Discovery likely also uses other methods (SSH/WMI); the &#x27;mostly&#x27; wording is not clearly false.; Device42 is now owned by Freshworks. That is optional context, not a correction.</p>

</details>

<h3>Infoblox — keep</h3>

<p>Source or watched-source coverage changed since research.</p>

<details>
<summary>Evidence and limitations</summary>

<p>infoblox.com is live and still positions the company around DDI (DNS, DHCP, IPAM) for networking, security and cloud. The description is accurate apart from subjective &#x27;industry leader&#x27; marketing phrasing.</p>

<p>https://www.infoblox.com/ — The page is titled &#x27;Infoblox - Future-Proof DDI to Unite Networking and Security&#x27;. It discusses enterprise-grade DDI, network visibility and DNS security.</p>

<p>Caveats: &#x27;Industry leader&#x27; is a subjective claim and was not evaluated.</p>

</details>

<h3>phpIPAM — keep</h3>

<p>Source or catalog stability was not confirmed for this review.</p>

<details>
<summary>Evidence and limitations</summary>

<p>phpipam.net is live and lists current version 1.9.0. It describes phpIPAM as a free, open-source web IPAM with a REST API, so the entry&#x27;s description is supported.</p>

<p>https://phpipam.net/ — Page title: &#x27;phpIPAM — Free Open Source IP Address Management Software&#x27;. It shows &#x27;Current version: 1.9.0&#x27; and &#x27;phpIPAM is a free, open source IP address management tool with IPv4/IPv6 support, VLAN management, REST API, and Docker deployment.&#x27;</p>

<p>Caveats: The phrase &#x27;light, modern and useful&#x27; is the project&#x27;s own subjective wording. I did not evaluate it.</p>

</details>

<h3>Ansible: Up and Running — keep</h3>

<p>Source snapshot unavailable.</p>

<details>
<summary>Evidence and limitations</summary>

<p>The legacy shop.oreilly.com URL redirects to O&#x27;Reilly&#x27;s library page for the 1st edition (ISBN 9781491915318), so the link still points to the book. A 3rd edition (2022) exists and covers network devices. The entry&#x27;s subtitle description is still accurate.</p>

<p>https://shop.oreilly.com/product/0636920035626.do — curl followed redirects to https://www.oreilly.com/library/view/~/9781491915318/, which returned 403 to automated clients (Akamai &#x27;Access Denied&#x27;).</p>

<p>https://www.oreilly.com/library/view/ansible-up-and/9781098109141/ — A search result shows &#x27;Ansible: Up and Running, 3rd Edition&#x27; (Meijer, Hochstein, Moser; 2022-07-12). The book covers managing Linux, Windows and network devices.</p>

<p>Caveats: O&#x27;Reilly blocks automated fetches (403), so I could not read the redirect target directly. This is a temporary or bot-blocking problem to recheck, not evidence that the page is dead.; Optionally, the maintainer could point the link at the 3rd edition&#x27;s canonical library URL. This is not required to fix a factual error.</p>

<p>Source snapshot incomplete; excluded from the saved baseline.</p>

</details>

<h3>Cloud Native Data Center Networking — keep</h3>

<p>Source snapshot unavailable.</p>

<details>
<summary>Evidence and limitations</summary>

<p>The entry&#x27;s description matches the publisher&#x27;s description word for word, according to search results. The book (Dinesh Dutt, O&#x27;Reilly, 2019) also covers network automation. The library URL returned 403 to automated clients only, which is bot-blocking.</p>

<p>https://www.oreilly.com/library/view/cloud-native-data/9781492045595/colophon01.html — A search result shows this O&#x27;Reilly page under the same ISBN path (&#x27;About the Author - Cloud Native Data Center Networking [Book]&#x27;), which confirms the URL path exists.</p>

<p>https://books.google.com/books/about/Cloud_Native_Data_Center_Networking.html?id=79i_DwAAQBAJ — The publisher&#x27;s description (&#x27;If you want to study, build, or simply validate your thinking about modern cloud native data center networks, this is your book...&#x27;) matches the entry. Its topics include network automation, with examples from FRR to Ansible.</p>

<p>Caveats: Direct fetches of the O&#x27;Reilly URL returned 403 Access Denied (Akamai), so this needs a recheck. It is not evidence the page is gone.; The book leans toward general networking. Its fit depends on its automation and open-networking content.</p>

<p>Source snapshot incomplete; excluded from the saved baseline.</p>

</details>

<h3>Effective DevOps — keep</h3>

<p>Source or catalog stability was not confirmed for this review.</p>

<details>
<summary>Evidence and limitations</summary>

<p>The Amazon page is live for &#x27;Effective DevOps: Building a Culture of Collaboration, Affinity, and Tooling at Scale&#x27; by Davis and Daniels. The description of cultural and organizational DevOps practices matches.</p>

<p>https://www.amazon.com/Effective-DevOps-Building-Collaboration-Affinity/dp/1491926309/ — Returns HTTP 200. The title shows &#x27;Effective DevOps: Building a Culture of Collaboration, Affinity, and Tooling at Scale: Davis, Jennifer, Daniels, Ryn: 9781491926307&#x27;.</p>

<p>Caveats: Amazon is a retail page. Its content can vary by region and bot detection.</p>

</details>

<h3>Infrastructure as Code — keep</h3>

<p>Source or catalog stability was not confirmed for this review.</p>

<details>
<summary>Evidence and limitations</summary>

<p>The Amazon page is live for &#x27;Infrastructure as Code: Managing Servers in the Cloud&#x27; by Kief Morris. The description (IaC principles and patterns, with compute rather than network examples) matches this 1st edition.</p>

<p>https://www.amazon.com/Infrastructure-Code-Managing-Servers-Cloud/dp/1491924357 — Returns HTTP 200. The product title is &#x27;Infrastructure as Code: Managing Servers in the Cloud&#x27;, by Kief Morris, ISBN 9781491924358.</p>

<p>Caveats: Newer editions of the book exist. Linking the latest edition is optional and does not correct a factual error.</p>

</details>

<h3>Mastering Python Networking Second Edition (August 2018) — keep</h3>

<p>Source or catalog stability was not confirmed for this review.</p>

<details>
<summary>Evidence and limitations</summary>

<p>Both affiliate short links resolve to live Amazon pages for Eric Chou&#x27;s Mastering Python Networking: the 2nd edition (Kindle, B07CB4LDKR) and the 1st edition (1784397008, subtitle includes &#x27;SDN&#x27;). The dated edition labels are historical and accurate, and the book is about Python network automation.</p>

<p>https://amzn.to/2PkMRiZ — Redirects to amazon.com/gp/product/B07CB4LDKR, which returns HTTP 200. The title reads &#x27;Mastering Python Networking: Your one-stop solution to using Python for network automation, DevOps, and Test-Driven Development 2, Chou, Eric&#x27;.</p>

<p>https://amzn.to/2NBjlVM — Redirects to amazon.com/gp/product/1784397008, which returns HTTP 200. The title reads &#x27;Mastering Python Networking: Your one stop solution to using Python for network automation, DevOps, and SDN: 9781784397005&#x27;. This matches the entry&#x27;s note about &#x27;more SDN-related topics&#x27;.</p>

<p>Caveats: This compound entry is not editable. Later editions exist; adding them would be an optional expansion, not a correction.; The links are Amazon affiliate short links (tag pythfornetwen-20).</p>

</details>

<h3>TeemIP — keep</h3>

<p>Source snapshot unavailable.</p>

<details>
<summary>Evidence and limitations</summary>

<p>The SourceForge project page blocks automated curl (403), but WebFetch could read it. TeemIP is an active open-source IPAM/DDI project built on iTop, with a release updated 2026-10-06. Its official site and GitHub org confirm IPv4/IPv6 IP management, subnet management, IP requests and discovery. The description is supported.</p>

<p>https://sourceforge.net/projects/teemip/ — Via WebFetch: &#x27;teemIP - CMDB &amp; DDI solution&#x27;, an open-source IPAM/DDI on iTop with IPv4 and IPv6 registration and subnet management. Latest file teemIP-3.3.0-2610.zip, updated October 6, 2026, AGPLv3. It links to www.teemip.net and github.com/TeemIp.</p>

<p>https://www.teemip.com/ — teemip.net redirects here. Title: &#x27;teemIP, Official Website | Open Source IPAM &amp; DDI with CMDB&#x27;.</p>

<p>https://wiki.teemip.net/doku.php?id=extensions:start — A search summary of the official wiki lists TeemIp extensions, including core IP management, IP request management (portal), IP discovery, DNS zone and DHCP management.</p>

<p>Caveats: curl returned 403 for SourceForge, which is bot-blocking. Content was read through WebFetch.; The description has a typo (&#x27;IP Adress&#x27;). The project now calls itself &#x27;teemIP&#x27; and describes itself more broadly as DDI + CMDB. Neither is a factual error in what the entry claims.</p>

<p>Source snapshot incomplete; excluded from the saved baseline.</p>

</details>

<h3>Network Programmability and Automation — keep</h3>

<p>Source snapshot unavailable.</p>

<details>
<summary>Evidence and limitations</summary>

<p>The legacy shop.oreilly.com URL redirects to O&#x27;Reilly&#x27;s library page for the 1st edition (ISBN 9781491931240). Search results confirm that page still exists. A 2nd edition (2023) also exists. The subtitle description is accurate, and the book is core network automation material.</p>

<p>https://shop.oreilly.com/product/0636920042082.do — curl followed redirects to https://www.oreilly.com/library/view/~/9781491931240/, which returned 403 to automated clients (bot-blocking).</p>

<p>https://www.oreilly.com/library/view/network-programmability-and/9781491931240/ — A search result shows &#x27;Network Programmability and Automation [Book]&#x27;, the 1st edition (2018), still in O&#x27;Reilly&#x27;s library.</p>

<p>https://www.oreilly.com/library/view/network-programmability-and/9781098110826/ — A search result shows &#x27;Network Programmability and Automation, 2nd Edition&#x27; (Oswalt, Adell, Lowe, Edelman; 2023-08-17).</p>

<p>Caveats: Direct O&#x27;Reilly fetches returned 403, so this needs a recheck.; Optionally, the maintainer could link the 2nd edition or the canonical library URL. Neither is required to fix a factual error.</p>

<p>Source snapshot incomplete; excluded from the saved baseline.</p>

</details>

<h3>Network Programmability with YANG — keep</h3>

<p>Source snapshot unavailable.</p>

<details>
<summary>Evidence and limitations</summary>

<p>The book&#x27;s full title, &#x27;Network Programmability with YANG: The Structure of Network Automation with YANG, NETCONF, RESTCONF, and gNMI&#x27; (Claise, Clarke, Lindblad; Addison-Wesley, 2019), matches the entry&#x27;s description exactly. It is core network automation content. The O&#x27;Reilly URL returned 403 to automated clients only.</p>

<p>https://www.pearson.com/en-us/subject-catalog/p/network-programmability-with-yang-the-structure-of-network-automation-with-yang-netconf-restconf-and-gnmi/P200000009517/9780135180396 — Publisher listing (via search): &#x27;Network Programmability with YANG: The Structure of Network Automation with YANG, NETCONF, RESTCONF, and gNMI&#x27;, by Claise, Clarke and Lindblad.</p>

<p>https://www.oreilly.com/library/view/network-programmability-with/9780135180471/ — Direct fetch returned HTTP 403 (Akamai Access Denied) for both curl and WebFetch.</p>

<p>Caveats: I could not read the O&#x27;Reilly library page because of bot-blocking. Recheck it before treating it as healthy or broken.</p>

<p>Source snapshot incomplete; excluded from the saved baseline.</p>

</details>

<h3>Seeking SRE: Conversations About Running Production Systems at Scale — keep</h3>

<p>Source or catalog stability was not confirmed for this review.</p>

<details>
<summary>Evidence and limitations</summary>

<p>The Amazon product page resolves with no redirect. It shows &#x27;Seeking SRE: Conversations About Running Production Systems at Scale&#x27; by David N. Blank-Edelman (ISBN 9781491978863). The description is a fair summary of a collection of SRE essays, and a book on SRE and operations fits the Books section next to the Google SRE books.</p>

<p>https://www.amazon.com/Seeking-SRE-Conversations-Running-Production/dp/1491978864 — HTTP 200 with no redirect. The page title is &#x27;Seeking SRE: Conversations About Running Production Systems at Scale: Blank-Edelman, David N.: 9781491978863&#x27;.</p>

<p>Caveats: I only read the page title and metadata from Amazon. I did not check the book&#x27;s content against the claim about &#x27;practitioners not working at Google&#x27;. That claim matches how the publisher has generally described the book.</p>

</details>

<h3>IP Fabric — keep</h3>

<p>Source or catalog stability was not confirmed for this review.</p>

<details>
<summary>Evidence and limitations</summary>

<p>IP Fabric is live at the same URL. It still describes vendor-neutral discovery and a read-only digital twin of on-prem and cloud networks, change management validation, and an open API to feed other tools and SoT. That matches the entry&#x27;s discovery, modelling, cloud/on-prem and API claims, and the product fits network automation.</p>

<p>https://ipfabric.io/ — &#x27;IP Fabric builds a read-only digital twin of your on-prem and cloud environments&#x27; and &#x27;Feed IP Fabric&#x27;s trusted, vendor-neutral data model into any workflow via our open API and enterprise-grade MCP server.&#x27; The navigation includes Discovery &amp; Context, Intelligence &amp; Validation, Planning &amp; Change Management and Source of Truth Accuracy. The announced release is IP Fabric 8.2.</p>

<p>Caveats: The homepage now uses &#x27;network digital twin&#x27; wording rather than &#x27;network assurance&#x27;. Snapshots weren&#x27;t named on the homepage, but change validation is. Optional rewording only.</p>

</details>

<h3>Cisco Meraki — keep</h3>

<p>Source snapshot unavailable.</p>

<details>
<summary>Evidence and limitations</summary>

<p>meraki.cisco.com now 301-redirects to a cisco.com page under /about/corporate-strategy-office/acquisitions/meraki/, which returns 403 to curl. WebFetch read it: the page says &#x27;Cisco Meraki is now on Cisco.com&#x27; and lists active Wireless, Switching, Secure SD-WAN and other cloud-managed product lines plus the Meraki dashboard. The product line is active and Meraki-managed networks are API-driven (the Dashboard API is listed separately in the catalog), so the entry still fits. &#x27;The leader&#x27; is promotional wording, not a factual error I could confirm.</p>

<p>https://meraki.cisco.com/ — HTTP 301 to https://www.cisco.com/site/us/en/about/corporate-strategy-office/acquisitions/meraki/index.html.</p>

<p>https://www.cisco.com/site/us/en/about/corporate-strategy-office/acquisitions/meraki/index.html — The page says &#x27;Cisco Meraki is now on Cisco.com&#x27; and lists Wireless, Switching, Secure SD-WAN, Hybrid Cloud, Cellular Gateways, Remote Work, Smart Cameras and Sensors, with a Meraki dashboard login.</p>

<p>https://developer.cisco.com/meraki/ — The Meraki Developer Hub is live: &#x27;Meraki APIs make it possible to rapidly deploy and manage networks at scale&#x27;. It notes OpenAPI v3 support.</p>

<p>Caveats: The redirect target sits under an &#x27;acquisitions&#x27; path, which may change, and partner blogs report the Meraki brand being folded into a unified Cisco Networking/Cloud brand. That is not officially confirmed, so no change is recommended now. Recheck later.; Optionally, the promotional &#x27;is the leader&#x27; wording could be made neutral. It isn&#x27;t a confirmed factual error.</p>

<p>Source snapshot incomplete; excluded from the saved baseline.</p>

</details>

<h3>Packet Pushers Show 402 — keep</h3>

<p>Source or catalog stability was not confirmed for this review.</p>

<details>
<summary>Evidence and limitations</summary>

<p>The listed URL redirects (HTTP 200) to the current Packet Pushers episode page. The page title is &#x27;Weekly Show 402: Building A Network Automation Framework&#x27;, which matches the entry. The episode covers how to build a network automation framework: automation principles, data models and schemas, and testing code.</p>

<p>https://packetpushers.net/podcasts/heavy-networking/HN402-building-a-network-automation-framework/ — The listed URL redirects here (200). Page title: &#x27;Weekly Show 402: Building A Network Automation Framework&#x27;. Meta description: &#x27;how to build a network automation framework... Guest Ken Celenza joins us to get into the details about automation principles, data models and schemas, testing code, and more.&#x27;</p>

<p>Caveats: The listed URL works only through a redirect. The canonical URL is https://packetpushers.net/podcasts/heavy-networking/HN402-building-a-network-automation-framework/ and the maintainer could switch to it if they want.; I didn&#x27;t listen to the audio.</p>

</details>

<h3>Packet Pushers Show 532 — keep</h3>

<p>Source or catalog stability was not confirmed for this review.</p>

<details>
<summary>Evidence and limitations</summary>

<p>The listed URL redirects (HTTP 200) to the episode page &#x27;Heavy Networking 532: Scrapli Is A Netmiko Alternative&#x27;. The guests are Carl Montanari and Dmitry Figol, as the entry says. The topic is scrapli, a Python CLI screen-scraping client for network device automation.</p>

<p>https://packetpushers.net/podcasts/heavy-networking/HN532-scrapli-is-a-netmiko-alternative/ — The listed URL redirects here (200). Title: &#x27;Heavy Networking 532: Scrapli Is A Netmiko Alternative&#x27;. Description: &#x27;Scrapli is a Python screen-scraping client for network devices to help enable automation... with two of its creators, Carl Montanari and Dmitry Figol.&#x27;</p>

<p>Caveats: The listed URL works only through a redirect to the canonical HN532 URL.; I didn&#x27;t listen to the audio.</p>

</details>

<h3>Packet Pushers Show 537 — keep</h3>

<p>Source or catalog stability was not confirmed for this review.</p>

<details>
<summary>Evidence and limitations</summary>

<p>The listed URL redirects (HTTP 200) to a Packet Pushers blog post titled &#x27;Ansible Or Terraform: Choose One&#x27;. The post is an excerpt from Heavy Networking episode 537 with Ned Bellavance and Josh VanDeraa and links to the full episode. So the description and the guest names match the linked page, and the topic is network automation tooling. The full episode also exists at its own page, &#x27;Heavy Networking 537: Ansible Vs. Terraform For Network Automation&#x27;. Pointing the entry there is optional, not a factual correction.</p>

<p>https://packetpushers.net/blog/ansible-or-terraform-choose-one/ — The listed URL redirects here (200). The post is titled &#x27;Ansible Or Terraform: Choose One&#x27; and says &#x27;Ned Bellavance and Josh VanDeraa share their opinions in this excerpt from the Packet Pushers&#x27; Heavy Networking podcast. To hear the full conversation, play episode 537.&#x27;</p>

<p>https://packetpushers.net/podcasts/heavy-networking/HN537-ansible-vs-terraform-for-network-automation/ — Full episode page (200), reached by redirect from the link inside the blog post. Title: &#x27;Heavy Networking 537: Ansible Vs. Terraform For Network Automation&#x27;. Guests: Ned Bellavance and Josh VanDeraa.</p>

<p>Caveats: The entry is named &#x27;Show 537&#x27; but links to an excerpt post rather than the full episode page. The maintainer may prefer the HN537 episode URL, which is titled &#x27;Ansible Vs. Terraform For Network Automation&#x27;.; I didn&#x27;t listen to the audio.</p>

</details>

<h3>Podcast__init Episode 117 — keep</h3>

<p>Source or catalog stability was not confirmed for this review.</p>

<details>
<summary>Evidence and limitations</summary>

<p>The podcastinit.com URL redirects (HTTP 200) to the pythonpodcast.com episode page. The page title is &#x27;NAPALM with David Barroso and Mircea Ulinic&#x27;, episode E117, dated 09 July 2017. Its chapters cover NAPALM and challenges in network automation. The entry is accurate, and it&#x27;s a dated historic resource.</p>

<p>https://www.pythonpodcast.com/episodepage/napalm-with-david-barosso-and-mircea-ulinic-episode-117 — The listed URL redirects here (200). Page shows &#x27;NAPALM with David Barroso and Mircea Ulinic - E117&#x27;, dated 09 July 2017. Chapters include &#x27;Introduction to Napalm&#x27;, &#x27;Challenges in Network Automation&#x27;, and &#x27;Architecting Napalm&#x27;.</p>

<p>Caveats: The listed URL is on the old podcastinit.com domain and depends on a redirect. The canonical page is on pythonpodcast.com.; I didn&#x27;t listen to the audio.</p>

</details>

<h3>Podcast__init Episode 232 — keep</h3>

<p>Source or catalog stability was not confirmed for this review.</p>

<details>
<summary>Evidence and limitations</summary>

<p>The URL redirects (HTTP 200) to the episode page &#x27;Network Automation At Enterprise Scale With Python&#x27;. On it, Antoine Fourmy describes eNMS, his open source platform for automating enterprise networks. Both the title and the guest match the entry.</p>

<p>https://www.pythonpodcast.com/episodepage/enms-network-automation-episode-232 — Title: &#x27;Network Automation At Enterprise Scale With Python&#x27;. Summary: &#x27;In this episode Antoine Fourmy describes his work on eNMS and how it can be used to automate enterprise grade networks.&#x27;</p>

<p>Caveats: The listed URL works only through a redirect to the /episodepage/ path.; I didn&#x27;t listen to the audio.</p>

</details>

</details>

The complete research records remain local. This inventory contains all recommendations and unresolved entries from the saved initial review.

[One-entry integration example](https://github.com/bromanko/awesome-network-automation/blob/codex/catalog-inventory-preview/.um/catalog-inventory/checked-example.md). Saved research with real discussion-history and patch checks.
