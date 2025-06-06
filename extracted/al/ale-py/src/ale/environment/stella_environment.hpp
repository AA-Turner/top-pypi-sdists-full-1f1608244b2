/* *****************************************************************************
 * A.L.E (Arcade Learning Environment)
 * Copyright (c) 2009-2013 by Yavar Naddaf, Joel Veness, Marc G. Bellemare and
 *   the Reinforcement Learning and Artificial Intelligence Laboratory
 * Released under the GNU General Public License; see License.txt for details.
 *
 * Based on: Stella  --  "An Atari 2600 VCS Emulator"
 * Copyright (c) 1995-2007 by Bradford W. Mott and the Stella team
 *
 * *****************************************************************************
 *  stella_environment.hpp
 *
 *  A class that wraps around the Stella core to provide users with a typical
 *  reinforcement learning environment interface.
 *
 **************************************************************************** */

#ifndef __STELLA_ENVIRONMENT_HPP__
#define __STELLA_ENVIRONMENT_HPP__

#include "ale/environment/ale_ram.hpp"
#include "ale/environment/ale_screen.hpp"
#include "ale/environment/ale_state.hpp"
#include "ale/environment/phosphor_blend.hpp"
#include "ale/environment/stella_environment_wrapper.hpp"
#include "ale/emucore/Event.hxx"
#include "ale/emucore/OSystem.hxx"
#include "ale/emucore/System.hxx"
#include "ale/emucore/Random.hxx"
#include "ale/common/Constants.h"
#include "ale/games/RomSettings.hpp"
#include "ale/common/Log.hpp"
#include "ale/common/ScreenExporter.hpp"

#include <cstddef>
#include <memory>

namespace ale {

class StellaEnvironment {
 public:
  StellaEnvironment(stella::OSystem* system, RomSettings* settings);

  /** Resets the system to its start state. */
  void reset();

  /** Returns a copy of the current environment state. Note that by default this **does**
   * include the PNRG for sticky actions. You can optionally include the PRNG by setting
   * `include_rng` to true. For planning you probably want to disable
   * sticky actions. The emulator is fully deterministic. */
  ALEState cloneState(bool include_rng = false);
  /** Restores a previously saved copy of the state. */
  void restoreState(const ALEState&);

  /** Applies the given actions (e.g. updating paddle positions when the paddle is used)
   *  and performs one simulation step in Stella. Returns the resultant reward. When
   *  frame skip is set to > 1, up the corresponding number of simulation steps are performed.
   *  Note that the post-act() frame number might not correspond to the pre-act() frame
   *  number plus the frame skip.
   */
  reward_t act(Action player_a_action, Action player_b_action,
               float paddle_a_strength = 1.0, float paddle_b_strength = 1.0);

  /** Applies the given continuous actions (e.g. updating paddle positions when
   * the paddle is used) and performs one simulation step in Stella. Returns the
   * resultant reward. When frame skip is set to > 1, up the corresponding
   * number of simulation steps are performed.  Note that the post-act() frame
   * number might not correspond to the pre-act() frame number plus the frame
   * skip.
   */

  /** This functions emulates a push on the reset button of the console */
  void softReset();

  /** Keep pressing the console select button for a given amount of time*/
  void pressSelect(size_t num_steps = 1);

  /** Set the difficulty according to the value.
   *  If the first bit is 1, then it will put the left difficulty switch to A (otherwise leave it on B)
   *  If the second bit is 1, then it will put the right difficulty switch to A (otherwise leave it on B)
   *
   *  This change takes effect at the immediate next time step.
   */
  void setDifficulty(difficulty_t value);

  /** Set the game mode according to the value. The new mode will not take effect until reset() is
   *  called */
  void setMode(game_mode_t value);

  /** Returns true if the ROM reported a terminal signal OR if the episode is truncated
   * (i.e., isGameTerminal() || isTruncated()).
   * This functions serves to be backwards compatible with previous versions of ALE. */
  bool isTerminal() const;

  /** Returns true if the ROM reported a terminal signal */
  bool isGameTerminal() const;

  /** Returns true if the episode is truncated, i.e., max number of frames is reached */
  bool isGameTruncated() const;

  /** Accessor methods for the environment state. */
  void setState(const ALEState& state);
  const ALEState& getState() const;

  /** Returns the current screen after processing (e.g. colour averaging) */
  const ALEScreen& getScreen() const { return m_screen; }

  /** Accessor methods for RAM. `setRAM` can be useful to alter the environment.
   *  For example, learning a causal model of RAM transitions, changing environment dynamics, etc. */
  void setRAM(size_t memory_index, byte_t value);
  const ALERAM& getRAM() const { return m_ram; }

  /** Returns the current audio frame */
  const std::vector<uint8_t>& getAudio() const { return m_sound; }

  int getFrameNumber() const { return m_state.getFrameNumber(); }
  int getEpisodeFrameNumber() const { return m_state.getEpisodeFrameNumber(); }

  stella::Random& getEnvironmentRNG() { return m_random; }

  // Returns the current difficulty switch setting in use by the environment.
  difficulty_t getDifficulty() const { return m_state.getDifficulty(); }

  // Returns the game mode value last specified to the environment.
  // This may not be the exact game mode that the ROM is currently running as
  // game mode changes only take effect when the environment is reset.
  game_mode_t getMode() const { return m_state.getCurrentMode(); }

  /** Returns a wrapper providing #include-free access to our methods. */
  std::unique_ptr<StellaEnvironmentWrapper> getWrapper();

 private:
  /** This applies an action exactly one time step. Helper function to act(). */
  reward_t oneStepAct(Action player_a_action, Action player_b_action,
                      float paddle_a_strength, float paddle_b_strength);

  /** Actually emulates the emulator for a given number of steps. */
  void emulate(Action player_a_action, Action player_b_action,
               float paddle_a_strength, float paddle_b_strength,
               size_t num_steps = 1);

  /** Drops illegal actions, such as the fire button in skiing. Note that this is different
   *   from the minimal set of actions. */
  void noopIllegalActions(Action& player_a_action, Action& player_b_action);

  /** Processes the current emulator screen and saves it in m_screen */
  void processScreen();
  /** Processes the current emulator audio and saves it in m_sound */
  void processAudio(size_t i_frame);
  /** Processes the emulator RAM and saves it in m_ram */
  void processRAM();

 private:
  stella::OSystem* m_osystem;
  RomSettings* m_settings;
  PhosphorBlend m_phosphor_blend; // For performing phosphor colour averaging, if so desired
  stella::Random m_random; // Environment random number generator, used for sticky actions
  std::string m_cartridge_md5; // Necessary for saving and loading emulator state

  ALEState m_state;   // Current environment state
  ALEScreen m_screen; // The current ALE screen (possibly colour-averaged)
  ALERAM m_ram;       // The current ALE RAM
  std::vector<uint8_t> m_sound; // The current audio frame

  bool m_use_paddles; // Whether this game uses paddles

  /** Parameters loaded from Settings. */
  int m_num_reset_steps;             // Number of RESET frames per reset
  bool m_colour_averaging;           // Whether to average frames
  int m_max_num_frames_per_episode;  // Maxmimum number of frames per episode
  size_t m_frame_skip;               // How many frames to emulate per act()
  float m_repeat_action_probability; // Stochasticity of the environment
  std::unique_ptr<ScreenExporter> m_screen_exporter; // Automatic screen recorder
  int m_max_lives;                  // Maximum number of lives at the start of an episode.
  bool m_truncate_on_loss_of_life;  // Whether to truncate episodes on loss of life.
  int m_reward_min;                // Minimum reward value
  int m_reward_max;                // Maximum reward value

  // The last actions taken by our players
  Action m_player_a_action, m_player_b_action;
  float m_paddle_a_strength, m_paddle_b_strength;
  float m_player_a_r, m_player_b_r;
  float m_player_a_theta, m_player_b_theta;
  float m_player_a_fire, m_player_b_fire;
};

}  // namespace ale

#endif  // __STELLA_ENVIRONMENT_HPP__
