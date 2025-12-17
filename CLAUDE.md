# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is **Python Turtle Math Adventure** - a 12-session Python programming tutorial for 9-year-olds with Scratch experience who love mathematics. The tutorial uses turtle graphics to teach programming concepts through visual, math-integrated projects.

## Architecture and Structure

The repository is organized as a **documentation/tutorial system** with the following key components:

### Core Documentation
- `README.md` - Entry point for users, overview of the 12-session course
- `overview.md` - Detailed course overview, pedagogy, learning outcomes, and structure
- `sessions/session01/` through `sessions/session12/` - Individual session guides
  - Each session includes: learning objectives, kid-friendly analogies, theory with code examples, hands-on exercises, math connections, challenge problems, and session checklist
- `parent_guides/` - Support materials for parents/teachers
  - `setup_guide.md` - Installation and technical setup instructions
  - `learning_tips.md` - Pedagogical approaches and teaching strategies
  - `faq.md` - Frequently asked questions and troubleshooting
  - `resources.md` - Additional learning resources and extensions
- `resources/cheatsheet.md` - Quick reference for Python turtle commands and programming concepts
- `code_examples/` - **Currently empty** - intended for storing student code examples

### Pedagogical Design
The course follows a **three-phase progression**:
1. **Phase 1 (Sessions 1-4)**: Programming Basics - turtle graphics, variables, input, loops
2. **Phase 2 (Sessions 5-8)**: Logic & Control - conditionals, functions, lists, advanced math
3. **Phase 3 (Sessions 9-12)**: Visual & Creative - animation, fractals, game design, final project

Each session connects programming concepts to **mathematics** (coordinate geometry, algebra, patterns, recursion) and uses **kid-friendly analogies** to explain abstract concepts.

### Content Patterns
Session files follow a consistent structure:
- Learning objectives with emoji indicators
- Kid-friendly analogies for each concept
- Theory sections with code examples
- Hands-on exercises with increasing difficulty
- Math connection callouts
- Scratch-to-Python translation tables
- Debugging tips
- Session checklist
- Challenge problems (Bronze, Silver, Gold levels)

## Common Development Tasks

### Editing Session Content
When modifying session files:
1. Maintain the consistent structure and emoji indicators
2. Ensure code examples are tested and work with Python 3.6+ and turtle module
3. Keep analogies age-appropriate (9-year-old level)
4. Preserve math connections throughout
5. Update the Scratch-to-Python translation tables when adding new concepts

### Adding New Sessions
If extending beyond 12 sessions:
1. Follow the existing session structure
2. Update `README.md`, `overview.md`, and any navigation references
3. Consider the pedagogical progression - new sessions should build on previous concepts

### Updating Parent Guides
Parent guides should be kept synchronized with session content:
- `setup_guide.md` should reflect any changes in software requirements
- `learning_tips.md` should align with teaching approaches in sessions
- `faq.md` should address common issues from actual usage
- `resources.md` should be periodically updated with current external resources

### Working with Code Examples
The `code_examples/` directory is intended for:
- Complete working examples from sessions
- Additional example programs
- Solution code for challenge problems

When adding code examples:
1. Include comments explaining key concepts
2. Test thoroughly with Python's turtle module
3. Consider adding alternative versions showing different approaches

## Technical Notes

### No Build System
This is a documentation repository - there is no build system, linting, or automated testing. Content validation is manual.

### Markdown Preview
To preview Markdown files locally:
```bash
# Using Python's http server for browsing
cd /home/tarun-bansal/PythonTurtleMathAdventure
python3 -m http.server 8000
# Then open http://localhost:8000 in browser

# Or use markdown preview tools like:
# - VS Code with Markdown Preview Enhanced
# - Typora
# - MarkText
```

### Link Validation
Check internal links between files manually or use tools like:
```bash
# Example using grep to find broken references
grep -r "session[0-9]" . --include="*.md" | grep -v "session[0-9][0-9]"
```

### Content Standards
- Use **emoji indicators** consistently (🎯, 🐢, 🔧, 📍, etc.)
- **Code blocks** should use Python syntax highlighting
- **Internal links** use relative paths
- **External links** should be to reliable, kid-appropriate resources
- **Images/diagrams** are not currently used but could be added to `resources/`

## Session Development Workflow

When creating or modifying content:

1. **Concept Alignment**: Ensure programming concepts connect to mathematics
2. **Age Appropriateness**: Language and examples suitable for 9-year-olds
3. **Visual Focus**: Emphasize turtle graphics and immediate visual feedback
4. **Progressive Difficulty**: Exercises should scaffold from simple to complex
5. **Debugging Support**: Include common errors and troubleshooting tips
6. **Creative Extension**: Provide opportunities for personalization and creativity

## Repository Maintenance

### Regular Updates
- Check that all Python code examples work with current Python versions
- Verify external links in `resources.md` and parent guides are still valid
- Consider adding translated versions if needed
- Update based on user feedback from actual teaching experiences

### Version Considerations
The tutorial assumes **Python 3.6+** and uses the standard library `turtle` module. Changes to Python or the turtle module in future versions may require updates to code examples.

### Contribution Guidelines
While not currently set up for external contributions, any additions should:
- Maintain the pedagogical approach and tone
- Be thoroughly tested with the target age group
- Include both programming and math learning objectives
- Follow the existing structure and formatting conventions