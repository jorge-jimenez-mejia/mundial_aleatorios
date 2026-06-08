"""
🏆 FIFA WORLD CUP 2026 DRAW 🏆
==============================

• 12 participants, 4 teams each
• Every person is guaranteed 1 elite team (Top 12)
• Run with: python world_cup_draw_live.py
"""

import random

# ══════════════════════════════════════════════════════════════

# CONFIGURATION

# ══════════════════════════════════════════════════════════════

NAMES = [
"Jorge",
"Saul",
"Danny",
"Juan Lara",
"Leo",
"Balfred",
"Uriel",
"Juan Jimenez",
"Angel",
"Shad",
"alexis",
"omar",
]

# ══════════════════════════════════════════════════════════════

# TEAMS

# ══════════════════════════════════════════════════════════════

ELITE_TEAMS = [
"France 🇫🇷",
"Spain 🇪🇸",
"Argentina 🇦🇷",
"England 🏴",
"Portugal 🇵🇹",
"Brazil 🇧🇷",
"Netherlands 🇳🇱",
"Belgium 🇧🇪",
"Germany 🇩🇪",
"Croatia 🇭🇷",
"Morocco 🇲🇦",
"Colombia 🇨🇴",
]

OTHER_TEAMS = [
"Uruguay 🇺🇾",
"Senegal 🇸🇳",
"Switzerland 🇨🇭",
"Mexico 🇲🇽",
"United States 🇺🇸",
"Japan 🇯🇵",
"Denmark 🇩🇰",
"Austria 🇦🇹",
"South Korea 🇰🇷",
"Iran 🇮🇷",
"Australia 🇦🇺",
"Ukraine 🇺🇦",
"Turkey 🇹🇷",
"Serbia 🇷🇸",
"Poland 🇵🇱",
"Canada 🇨🇦",
"Ecuador 🇪🇨",
"Peru 🇵🇪",
"Chile 🇨🇱",
"Paraguay 🇵🇾",
"Venezuela 🇻🇪",
"Panama 🇵🇦",
"Costa Rica 🇨🇷",
"Honduras 🇭🇳",
"Jamaica 🇯🇲",
"Dominican Republic 🇩🇴",
"Nigeria 🇳🇬",
"Ghana 🇬🇭",
"Cameroon 🇨🇲",
"Ivory Coast 🇨🇮",
"Tunisia 🇹🇳",
"Algeria 🇩🇿",
"Saudi Arabia 🇸🇦",
"Iraq 🇮🇶",
"New Zealand 🇳🇿",
"Bolivia 🇧🇴",
]

# ══════════════════════════════════════════════════════════════

# HELPER FUNCTIONS

# ══════════════════════════════════════════════════════════════

def clear_screen():
    """Print blank lines to simulate a clean screen."""
    print("\n" * 3)

def separator(char="═", width=56):
    """Print a separator line."""
    print(char * width)

def run_draw(names):
    """Run the draw and return results."""

    elite_pool = ELITE_TEAMS[:]
    other_pool = OTHER_TEAMS[:]

    random.shuffle(elite_pool)
    random.shuffle(other_pool)

    results = []

    for i, name in enumerate(names):
        elite = elite_pool[i]

        others = [
            other_pool[i * 3 + j]
            for j in range(3)
        ]

        # Keep elite separate for later reveal
        results.append(
            {
                "name": name,
                "others": others,
                "elite": elite,
            }
        )

    return results


def reveal_results(results):
    """Reveal normal teams first, then elite teams."""

    # ═══════════════════════════════════════
    # ROUND 1 — NORMAL TEAMS
    # ═══════════════════════════════════════

    separator("═", 60)
    print("   🎲  ROUND 1 — NORMAL TEAMS  🎲")
    separator("═", 60)

    print("\nPress Enter to reveal teams...\n")

    for result in results:
        separator()

        print(f"  🎽  {result['name'].upper()}")

        separator()

        for index, team in enumerate(result["others"], start=1):
            input(f"    [{index}/3] Press Enter → ")

            print(f"    •   {team}")
            print()

        input("  Press Enter for the next participant...")

        clear_screen()

    # ═══════════════════════════════════════
    # ROUND 2 — ELITE TEAMS
    # ═══════════════════════════════════════

    separator("═", 60)
    print("   ⭐  FINAL ROUND — ELITE TEAMS  ⭐")
    separator("═", 60)

    print("\nNow revealing the elite teams...\n")

    input("Press Enter to continue...")

    clear_screen()

    for result in results:
        separator()

        print(f"  🎽  {result['name'].upper()}")

        separator()

        input("\n  Press Enter to reveal elite team → ")

        print(f"\n    ⭐  {result['elite']}  ← ELITE TEAM\n")

        input("  Press Enter for the next participant...")

        clear_screen()


def final_summary(results):
    """Print final summary."""

    clear_screen()

    separator("═", 70)

    print("  📋  FINAL SUMMARY — FIFA WORLD CUP 2026 DRAW")

    separator("═", 70)

    print(
        f"\n  {'PARTICIPANT':<18} "
        f"{'ELITE TEAM ⭐':<28} "
        f"{'OTHER TEAMS'}"
    )

    separator("─", 70)

    for result in results:
        others_str = " | ".join(result["others"])

        print(
            f"  {result['name']:<18} "
            f"{result['elite']:<28} "
            f"{others_str}"
        )

    separator("─", 70)

    print("\n  ⭐ = guaranteed Top 12 elite team")

    print(f"\n  Top 12: {', '.join(ELITE_TEAMS)}")

    separator("═", 70)

def save_txt(results):
    """Save results to a .txt file."""

    filename = "draw_results.txt"

    with open(filename, "w", encoding="utf-8") as file:
        file.write("FIFA WORLD CUP 2026 DRAW\n")
        file.write("=" * 50 + "\n\n")

        for result in results:
            file.write(f"{result['name']}:\n")

            for team in result["others"]:
                file.write(f"   • {team}\n")

                file.write(f"   ⭐ {result['elite']} (elite)\n")

            file.write("\n")

    print(f"\n  💾 Results saved to: {filename}")

# ══════════════════════════════════════════════════════════════

# MAIN

# ══════════════════════════════════════════════════════════════

def main():
    separator("═", 56)

    print("   🏆   FIFA WORLD CUP 2026 DRAW   🏆")

    separator("═", 56)

    print("   12 participants  •  4 teams per person")
    print("   1 elite team guaranteed per participant")

    separator("─", 56)

    names = NAMES[:]

    # Randomize participant reveal order
    random.shuffle(names)

    print("\n  Participants:\n")

    for index, name in enumerate(names, start=1):
        print(f"    {index:>2}. {name}")

    print("\nReady for the draw? Press Enter to begin...")

    input()

    results = run_draw(names)

    clear_screen()

    separator("═", 56)

    print("   🎲  LET THE DRAW BEGIN!  🎲")

    separator("═", 56)

    reveal_results(results)

    input("\nPress Enter to view the final summary...")

    final_summary(results)

    print("\nSave results to a .txt file? [Y/N]")

    if input("→ ").strip().upper() == "Y":
        save_txt(results)

    print("\n  Good luck everyone! ⚽🏆\n")


if __name__ == "__main__":
    main()
