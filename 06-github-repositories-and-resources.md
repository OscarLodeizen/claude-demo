# Claude Skills: GitHub Repositories & Resources Guide

## Overview

This comprehensive guide catalogs the best GitHub repositories for Claude Skills, organized by type and use case. These resources will help you build production-ready automation solutions faster by leveraging existing skills and learning from community examples.

**Last Updated**: November 2025

## Official Anthropic Resources

### 1. anthropics/skills ⭐ Official
**URL**: https://github.com/anthropics/skills

**Description**: The official public repository for Claude Skills from Anthropic.

**What's Included**:
- Reference examples for complex skills
- Pre-built skills that ship with Claude:
  - Microsoft Word (docx)
  - Microsoft PowerPoint (pptx)
  - Microsoft Excel (xlsx)
  - PDF generation
- Skills demonstrating binary file formats
- Document structure handling examples

**Example Skills**:
- `algorithmic-art`: Creating generative art using p5.js
- `canvas-design`: Visual art in PNG and PDF formats
- `slack-gif-creator`: Animated GIFs optimized for Slack
- `artifacts-builder`: Complex HTML artifacts with React, Tailwind CSS, shadcn/ui
- `mcp-server`: MCP server integration examples
- `webapp-testing`: Testing local web applications with Playwright
- `brand-guidelines`: Applying company branding to outputs
- `internal-comms`: Internal communication templates

**Usage**:
```bash
# Register as Claude Code plugin marketplace
/plugin marketplace add anthropics/skills

# Install specific skill
/plugin install [skill-name]@anthropics/skills
```

**Best For**:
- Learning skill structure and best practices
- Understanding Anthropic's approach to complex skills
- Starting templates for custom development
- Production-ready document generation

**License**: MIT (typical for Anthropic projects)

---

## Curated Awesome Lists

### 2. travisvn/awesome-claude-skills ⭐ Recommended
**URL**: https://github.com/travisvn/awesome-claude-skills

**Description**: Most comprehensive curated list of Claude Skills, resources, and tools - particularly focused on Claude Code.

**Highlights**:
- **obra/superpowers**: 20+ battle-tested skills (featured prominently)
- TDD, debugging, and collaboration patterns
- Slash commands: /brainstorm, /write-plan, /execute-plan
- Skills-search tool for discovery
- Extensive documentation and tutorials
- Regularly updated with community contributions

**Categories Covered**:
- Development workflows
- Testing and debugging
- Document processing
- Creative/design skills
- Business automation
- Security and compliance

**Best For**:
- Discovering new skills
- Finding battle-tested solutions
- Learning best practices
- Community-driven quality

**Unique Features**:
- Quality curation (not just quantity)
- Focus on Claude Code workflows
- Integration with obra/superpowers ecosystem
- Regular community updates

### 3. ComposioHQ/awesome-claude-skills
**URL**: https://github.com/ComposioHQ/awesome-claude-skills

**Description**: Curated list of practical Claude Skills for enhancing productivity across all Claude platforms.

**What's Included**:
- Document processing skills (docx, pdf, pptx, xlsx)
- Development workflow automation
- Specialized productivity tools
- API integration examples
- Cross-platform skills (Claude.ai, Claude Code, API)

**Categories**:
- **Pre-Built Skills**: Official Anthropic skills
- **Development Tools**: Git, testing, debugging
- **Document Automation**: Office suite integration
- **Data Analysis**: CSV, JSON, database tools
- **Creative Tools**: Image, video, design

**Best For**:
- Business productivity automation
- Office document workflows
- Cross-platform skill deployment

### 4. BehiSecc/awesome-claude-skills
**URL**: https://github.com/BehiSecc/awesome-claude-skills

**Description**: Security-focused curated collection of Claude Skills.

**Key Skills**:
- **git-pushing**: Git workflow automation
- **test-driven-development**: TDD implementation
- **systematic-debugging**: Structured debugging approach
- **webapp-testing**: Web application testing
- Security testing patterns
- Code review automation

**Best For**:
- Security-conscious development
- DevSecOps workflows
- Testing and quality assurance

### 5. abubakarsiddik31/claude-skills-collection
**URL**: https://github.com/abubakarsiddik31/claude-skills-collection

**Description**: Comprehensive collection combining official and community-built skills.

**Unique Value**:
- Mixed official + community skills
- Well-organized by category
- Production examples
- Documentation quality focus

**Best For**:
- One-stop skill discovery
- Finding diverse skill types
- Comparing official vs. community approaches

---

## Production-Ready Skill Libraries

### 6. obra/superpowers ⭐ Essential
**URL**: https://github.com/obra/superpowers

**Description**: Core skills library for Claude Code - the gold standard for development workflows.

**Author**: Jesse Vincent (obra)
**Version**: 3.4.1+
**License**: MIT

**Core Capabilities**:

**Testing Skills**:
- `test-driven-development`: RED/GREEN TDD workflow
- `async-testing`: Asynchronous test patterns
- `anti-patterns`: Common testing mistakes to avoid

**Debugging Skills**:
- `systematic-debugging`: Structured debugging approach
- `root-cause-tracing`: Finding underlying issues
- `verification`: Confirming fixes work

**Collaboration Skills**:
- `brainstorming`: Structured ideation
- `planning`: Project and feature planning
- `code-review`: Automated code review patterns
- `parallel-agents`: Multi-agent coordination

**Development Skills**:
- `using-git-worktrees`: Isolated git environments
- `finishing-branches`: Complete feature branches
- `subagent-workflows`: Complex multi-step automation

**Meta Skills**:
- Creating new skills
- Testing skills
- Sharing skills with team

**Installation**:
```bash
# Register marketplace
/plugin marketplace add obra/superpowers-marketplace

# Install superpowers
/plugin install superpowers@superpowers-marketplace
```

**Slash Commands**:
- `/superpowers:brainstorm` - Structured brainstorming sessions
- `/superpowers:write-plan` - Create implementation plans
- `/superpowers:execute-plan` - Execute planned tasks

**Key Features**:
- **Automatic Activation**: Skills load when relevant
- **TDD by Default**: Write tests first, then implementation
- **Git Workflow Integration**: Smart branching and merging
- **Questioning Process**: Claude asks before writing code

**Real-World Usage**:
- Production deployments across companies
- Battle-tested in real codebases
- Active community contributions
- Regular updates and improvements

**Best For**:
- Software development teams
- TDD practitioners
- Git-heavy workflows
- Senior developer-level automation

**Related Projects**:
- `obra/superpowers-marketplace`: Curated plugin marketplace
- `jpcaparas/superpowers-laravel`: Laravel-specific extensions
- Multiple community forks for specific frameworks

### 7. alirezarezvani/claude-skills
**URL**: https://github.com/alirezarezvani/claude-skills

**Description**: 42 production-ready skills for real-world business usage.

**Focus Areas**:
- Marketing automation
- Executive leadership support
- Product development workflows
- Business operations

**Skill Categories**:

**Marketing Skills**:
- Content creation
- SEO optimization
- Campaign planning
- Social media management

**Executive Skills**:
- Strategic planning
- Meeting facilitation
- Decision frameworks
- Stakeholder communications

**Product Skills**:
- Roadmap planning
- Feature specification
- User story creation
- Product documentation

**Development Skills**:
- Claude Code subagents
- Custom slash commands
- Workflow automation

**Key Differentiators**:
- **Business-Focused**: Not just developer tools
- **Production-Ready**: Used in real businesses
- **Modular Design**: Self-contained packages
- **Domain Expertise**: Specialized knowledge embedded

**Best For**:
- Business teams (non-technical)
- Product managers
- Marketing departments
- Executive assistants

### 8. alirezarezvani/claude-code-skill-factory
**URL**: https://github.com/alirezarezvani/claude-code-skill-factory

**Description**: Comprehensive toolkit for building production-ready Claude Skills at scale.

**What It Provides**:
- **Structured Templates**: Pre-built skill scaffolding
- **Code Agents**: Multi-agent workflow templates
- **Slash Commands**: Custom command generator
- **LLM Prompts**: Optimized prompt library
- **Build Tools**: Automation for skill creation

**Features**:
- Clean, developer-friendly setup
- Workflow integration automation
- Production deployment patterns
- Scalable architecture

**Use Cases**:
- Creating skill libraries for organizations
- Rapid skill prototyping
- Standardizing skill development
- Team collaboration on skills

**Best For**:
- Teams building many custom skills
- Skill development at scale
- Standardized skill architecture
- Developer tooling

---

## Specialized Frameworks & Tools

### 9. wshobson/agents
**URL**: https://github.com/wshobson/agents

**Description**: Intelligent automation and multi-agent orchestration for Claude Code.

**Components**:
- 85 specialized AI agents
- 15 multi-agent workflow orchestrators
- 47 agent skills
- 44 development tools
- 63 focused, single-purpose plugins

**Architecture**:
- Modular agent design
- Orchestration layer for complex workflows
- Plugin ecosystem
- Extensible framework

**Best For**:
- Enterprise-scale automation
- Complex multi-agent workflows
- Comprehensive tooling needs
- Large development teams

### 10. FrancyJGLisboa/agent-skill-creator
**URL**: https://github.com/FrancyJGLisboa/agent-skill-creator

**Description**: Meta-skill that teaches Claude Code to create complete agents autonomously.

**Capabilities**:
- Autonomous agent creation
- Production-ready code generation
- Self-contained agent packages
- Installation-ready output

**Workflow**:
1. Describe desired agent capability
2. Claude creates complete agent
3. Generated agent is production-ready
4. Install and use immediately

**Best For**:
- Rapid agent prototyping
- Non-developers creating agents
- Quick proof-of-concepts
- Learning agent architecture

### 11. metaskills/skill-builder
**URL**: https://github.com/metaskills/skill-builder

**Description**: Claude Code Agent Skills Builder - streamlined skill development.

**Features**:
- Guided skill creation process
- Template-based generation
- Best practices enforcement
- Testing framework integration

**Best For**:
- Learning skill development
- Consistent skill structure
- Team skill standards
- Quality assurance

### 12. sean-rowe/claude-code-agents
**URL**: https://github.com/sean-rowe/claude-code-agents

**Description**: Production-ready agents for DDD, BDD, and complete agile workflow automation.

**Methodologies Supported**:
- **Domain-Driven Design (DDD)**
- **Behavior-Driven Development (BDD)**
- **Agile/Scrum workflows**

**Included Agents**:
- User story creation
- Acceptance criteria definition
- Domain modeling
- Test scenario generation
- Sprint planning automation

**Best For**:
- Agile development teams
- DDD/BDD practitioners
- Enterprise software development
- Process-driven organizations

---

## Framework-Specific Skills

### 13. jpcaparas/superpowers-laravel
**URL**: https://github.com/jpcaparas/superpowers-laravel

**Description**: obra/superpowers adapted for Laravel development.

**Laravel-Specific Skills**:
- Eloquent model generation
- Migration creation
- Controller scaffolding
- Laravel testing patterns
- Artisan command helpers

**Best For**:
- Laravel developers
- PHP web applications
- MVC pattern enforcement

---

## Additional Resources & Tools

### 14. hesreallyhim/awesome-claude-code
**URL**: https://github.com/hesreallyhim/awesome-claude-code

**Description**: Curated list of commands, files, and workflows for Claude Code.

**Unique Content**:
- Slash command collection
- Workflow patterns
- Hook examples (SessionStart, etc.)
- Infrastructure showcases

**Featured Technique**:
- Context-aware skill activation using hooks
- Intelligent skill selection patterns

**Best For**:
- Advanced Claude Code usage
- Hook development
- Workflow optimization

### 15. Cranot/claude-code-guide
**URL**: https://github.com/Cranot/claude-code-guide

**Description**: Comprehensive guide to Claude Code best practices.

**Content**:
- Setup instructions
- Configuration best practices
- Skill development tutorial
- Troubleshooting guides
- Performance optimization

**Best For**:
- Beginners learning Claude Code
- Team onboarding
- Reference documentation

### 16. simonw/claude-skills
**URL**: https://github.com/simonw/claude-skills

**Description**: Contents of /mnt/skills in Claude's code interpreter environment.

**Value**:
- Understanding Claude's internal skill system
- Reverse engineering skill structure
- Learning from Claude's own skills

**Best For**:
- Advanced skill developers
- Understanding skill internals
- Research and learning

---

## Community Marketplaces

### 17. obra/superpowers-marketplace
**URL**: https://github.com/obra/superpowers-marketplace

**Description**: Curated Claude Code plugin marketplace.

**Purpose**:
- Centralized skill distribution
- Quality-curated plugins
- Easy installation
- Version management

**Usage**:
```bash
/plugin marketplace add obra/superpowers-marketplace
/plugin search [keyword]
/plugin install [skill-name]@superpowers-marketplace
```

**Best For**:
- Discovering vetted skills
- Easy skill installation
- Marketplace approach to skills

---

## How to Choose the Right Repository

### Decision Framework

**For Learning & Getting Started**:
1. Start with **anthropics/skills** (official examples)
2. Read **Cranot/claude-code-guide** (comprehensive guide)
3. Explore **travisvn/awesome-claude-skills** (curated discovery)

**For Software Development**:
1. Install **obra/superpowers** (essential toolkit)
2. Add framework-specific (e.g., **superpowers-laravel**)
3. Consider **sean-rowe/claude-code-agents** (DDD/BDD/Agile)

**For Business Automation**:
1. Start with **alirezarezvani/claude-skills** (42 business skills)
2. Use **ComposioHQ/awesome-claude-skills** (productivity focus)
3. Reference **anthropics/skills** (official document skills)

**For Building Custom Skills at Scale**:
1. Use **alirezarezvani/claude-code-skill-factory** (toolkit)
2. Consider **metaskills/skill-builder** (guided creation)
3. Try **FrancyJGLisboa/agent-skill-creator** (autonomous generation)

**For Enterprise Deployments**:
1. Deploy **wshobson/agents** (comprehensive framework)
2. Customize **obra/superpowers** (core workflows)
3. Build custom with **skill-factory** (your requirements)

**For Security-Focused Work**:
1. Review **BehiSecc/awesome-claude-skills** (security focus)
2. Use **obra/superpowers** testing skills
3. Add security-specific custom skills

---

## Installation & Setup Guide

### Method 1: Direct Plugin Installation

```bash
# In Claude Code

# Add a marketplace
/plugin marketplace add [github-user]/[repo-name]

# List available plugins
/plugin list

# Install specific plugin
/plugin install [skill-name]@[marketplace-name]

# Example: Installing superpowers
/plugin marketplace add obra/superpowers-marketplace
/plugin install superpowers@superpowers-marketplace
```

### Method 2: Manual Installation

```bash
# Clone repository to local machine
git clone https://github.com/[user]/[repo-name]

# Copy skills to Claude Code skills directory
cp -r [repo-name]/skills/* ~/.config/claude/skills/

# Or create symlink
ln -s /path/to/[repo-name]/skills ~/.config/claude/skills/[skill-name]
```

### Method 3: Repository Registration

For repositories with `.claude-plugin/plugin.json`:

```bash
# Register entire repository as plugin source
/plugin marketplace add [github-user]/[repo-name]
```

---

## Skill Development Best Practices

### Learning from Top Repositories

**1. Structure (from anthropics/skills)**:
```
skill-name/
├── SKILL.md              # Main instructions
├── README.md             # Documentation
├── examples/             # Usage examples
├── scripts/              # Helper scripts
└── resources/            # Supporting files
```

**2. SKILL.md Format (from obra/superpowers)**:
```markdown
---
name: skill-name
description: Brief description
version: 1.0.0
author: Your Name
triggers:
  - keyword1
  - keyword2
---

# Skill Name

## Purpose
What this skill does

## When to Use
Activation conditions

## Instructions
Step-by-step process

## Examples
Usage examples

## Edge Cases
Exception handling
```

**3. Testing (from obra/superpowers TDD)**:
- Include test cases in skill
- Verify skill activation
- Test edge cases
- Validate outputs

**4. Documentation (from community best practices)**:
- Clear README with usage examples
- Installation instructions
- Dependencies list
- Troubleshooting guide
- Contribution guidelines

---

## Comparison Matrix

| Repository | Type | Skill Count | Focus | Best For | Difficulty |
|-----------|------|-------------|-------|----------|------------|
| anthropics/skills | Official | ~10 | Reference | Learning | Beginner |
| obra/superpowers | Library | 20+ | Development | Developers | Intermediate |
| alirezarezvani/claude-skills | Library | 42 | Business | Business Users | Beginner |
| wshobson/agents | Framework | 85+ | Enterprise | Large Teams | Advanced |
| skill-factory | Toolkit | Templates | Creation | Skill Builders | Intermediate |
| awesome-claude-skills | Curated | 100+ | Discovery | Everyone | All Levels |
| superpowers-marketplace | Marketplace | Growing | Distribution | Consumers | Beginner |

---

## Trending & Emerging

### Recently Popular
1. **obra/superpowers**: Becoming standard for development
2. **anthropics/skills**: Official reference growing
3. **skill-factory**: Scalable development gaining traction

### Watch These
- New official Anthropic skills
- Framework-specific extensions
- Industry-specific skill libraries
- AI agent orchestration frameworks

### Community Growth
- Discord/Slack communities forming
- Regular skill showcase events
- Contribution guidelines maturing
- Quality standards emerging

---

## Contributing to Community

### How to Share Your Skills

**1. Submit to Awesome Lists**:
- Fork awesome-claude-skills repository
- Add your skill with description
- Submit pull request
- Follow contribution guidelines

**2. Create Plugin Repository**:
- Structure with `.claude-plugin/plugin.json`
- Write comprehensive README
- Include examples and tests
- Tag releases for versioning

**3. Share in Marketplaces**:
- Submit to obra/superpowers-marketplace
- Follow quality guidelines
- Maintain documentation
- Provide support

### Quality Standards

**For Community Acceptance**:
- [ ] Clear documentation
- [ ] Working examples included
- [ ] Tested in production
- [ ] Open source license
- [ ] Responsive maintenance
- [ ] Follows community standards
- [ ] Security considerations addressed

---

## Additional Learning Resources

### Official Documentation
- **Anthropic Docs**: https://docs.anthropic.com/
- **Skills Guide**: https://docs.anthropic.com/en/api/skills-guide
- **Claude Code Docs**: https://code.claude.com/docs/en/skills

### Community Resources
- **Blog Posts**: Simon Willison's analysis of Skills
- **YouTube**: Tutorial videos on skill creation
- **Udemy**: "Claude Code Beginner to Pro" course
- **Medium**: Various skill development articles

### Tools & SDKs
- Anthropic Python SDK: `pip install anthropic`
- Anthropic TypeScript SDK: `npm install @anthropic-ai/sdk`

---

## Conclusion

The Claude Skills ecosystem is rapidly maturing with high-quality repositories emerging across multiple use cases. For business automation focused on repeatable tasks:

**Essential Starting Point**:
1. **anthropics/skills** - Official reference
2. **obra/superpowers** - Development workflows
3. **alirezarezvani/claude-skills** - Business operations

**For Scaling**:
4. **skill-factory** - Build your library
5. **wshobson/agents** - Enterprise framework

**Stay Current**:
- Watch anthropics/skills for new official releases
- Follow obra/superpowers for development best practices
- Monitor awesome lists for community innovations

The ecosystem is evolving rapidly with new skills and frameworks appearing regularly. Bookmark the awesome lists and check them monthly for updates.

---

*Last Updated: November 2025*
*Source: GitHub repository analysis, community research, and official documentation*
