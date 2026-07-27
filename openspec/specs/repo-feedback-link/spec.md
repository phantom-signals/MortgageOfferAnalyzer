# repo-feedback-link Specification

## Purpose
Where a user of the hosted page goes with questions, feature requests, and bug reports: a footer line pointing at the tool's GitHub repository, its placement and styling relative to the existing glossary and disclaimer text, and the rule that it touches no computed figure.

## Requirements
### Requirement: Page points feedback at the source repository
The footer SHALL carry a line directing questions, comments, feature requests, and bug reports to the tool's GitHub repository, linked as `https://github.com/phantom-signals/MortgageOfferAnalyzer`. The line SHALL sit below the existing glossary and disclaimer text, and SHALL use the footer's existing type scale and link styling so it does not compete with the tool's inputs or results.

#### Scenario: Link present and reachable
- **WHEN** the page is loaded, by any means, and scrolled to the footer
- **THEN** a line naming questions, requests, and bug reports is displayed
- **AND** it contains an anchor to the repository URL
- **AND** the anchor is keyboard-focusable and reads as a link to a screen reader

#### Scenario: Unobtrusive placement
- **WHEN** the page is loaded
- **THEN** the feedback line is not visible above the fold on a desktop viewport
- **AND** it renders at the footer's small type size and muted color, not as a banner, dialog, or floating control

#### Scenario: Hosted and offline use
- **WHEN** the file is opened from disk with no network
- **THEN** the line still renders and the anchor still resolves to the repository URL
- **AND** nothing is fetched to display it

### Requirement: Feedback line changes no computed value
Adding the footer line SHALL NOT alter any input, computed figure, verdict, tooltip, or self-check outcome.

#### Scenario: Self-check unaffected
- **WHEN** the self-check runs after the line is added
- **THEN** it passes
- **AND** the existing assertion that every rendered label and readout row resolves to a definition is not tripped by the new text
