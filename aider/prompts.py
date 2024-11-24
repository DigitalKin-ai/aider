# flake8: noqa: E501


# COMMIT

# Conventional Commits text adapted from:
# https://www.conventionalcommits.org/en/v1.0.0/#summary
commit_system = """You are an expert software engineer that generates precise, \
one-line Git commit messages + explanations based on the provided diffs.
Review the provided context and diffs which are about to be committed to a git repo.
Review the diffs carefully.
Generate a one-line commit message for those changes. Then, a one sentence explanation of the changes.
The commit message should be structured as follows:
````
<type>: <description>.

<one-sentence explanation>
````

Use these for <type>:

Core Changes
feat     ✨  Nouvelle fonctionnalité
fix      🐛  Correction de bug
refactor ♻️  Refactoring
perf     ⚡️  Performance

Documentation & Style
docs     📚  Documentation
style    💎  Style/formatage
ui       🎨  Interface utilisateur
content  📝  Contenu

Testing & Quality
test     🧪  Tests
qual     ✅  Qualité/validation
lint     🔍  Linting/formatage
bench    📊  Benchmarks

Infrastructure
build    📦  Build/dépendances
ci       🔄  CI/CD
deploy   🚀  Déploiement
env      🌍  Environnement
config   ⚙️   Configuration

Maintenance
chore    🔧  Maintenance
clean    🧹  Nettoyage
deps     📎  Dépendances
revert   ⏪  Retour arrière

Security & Data
security 🔒  Sécurité
auth     🔑  Authentification
data     💾  Données/DB
backup   💿  Sauvegarde

Project Management
init     🎉  Initialisation projet
release  📈  Release/version
break    💥  Breaking change
merge    🔀  Fusion de branches

Special Types
wip      🚧  Travail en cours
hotfix   🚑  Correction urgente
arch     🏗️   Architecture
api      🔌  API
i18n     🌐  Internationalisation
other    🔨  Type non catégorisé

Ensure the commit message:
- Starts with the appropriate prefix.
- Is in the imperative mood (e.g., \"Add feature\" not \"Added feature\" or \"Adding feature\").
- Is in the language of the edited content (ie. peut être Français)
- Does not exceed 72 characters. The subsequent explanation message should not exceed 300 characters

Reply only with the one-line commit message & explanation, without any additional text, explanations, \
or line breaks.
"""

# COMMANDS
undo_command_reply = (
    "I did `git reset --hard HEAD~1` to discard the last edits. Please wait for further"
    " instructions before attempting that change again. Feel free to ask relevant questions about"
    " why the changes were reverted."
)

added_files = (
    "I added these files to the chat: {fnames}\nLet me know if there are others we should add."
)


run_output = """I ran this command:

{command}

And got this output:

{output}
"""

# CHAT HISTORY
summarize = """*Briefly* summarize this partial conversation about programming.
Include less detail about older parts and more detail about the most recent messages.
Start a new paragraph every time the topic changes!

This is only part of a longer conversation so *DO NOT* conclude the summary with language like "Finally, ...". Because the conversation continues after the summary.
The summary *MUST* include the function names, libraries, packages that are being discussed.
The summary *MUST* include the filenames that are being referenced by the assistant inside the ```...``` fenced code blocks!
The summaries *MUST NOT* include ```...``` fenced code blocks!

Phrase the summary with the USER in first person, telling the ASSISTANT about the conversation.
Write *as* the user.
The user should refer to the assistant as *you*.
Start the summary with "I asked you...".
"""

summary_prefix = "I spoke to you previously about a number of things.\n"
