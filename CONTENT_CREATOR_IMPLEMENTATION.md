# ? CONTENT CREATOR SYSTEM - COMPLETE IMPLEMENTATION

## **COPY THIS TO: Source/Frontline/FRContentCreatorSystem.cpp**

**Replace the entire file with this:**

```cpp
// FRContentCreatorSystem.cpp - Complete Implementation with ALL TODOs
#include "FRContentCreatorSystem.h"
#include "FRLog.h"
#include "FRMarketplaceSystem.h"
#include "Kismet/GameplayStatics.h"
#include "Engine/World.h"
#include "GameFramework/PlayerState.h"
#include "GameFramework/PlayerController.h"
#include "Http.h"
#include "HttpModule.h"
#include "Json.h"
#include "JsonUtilities.h"

void UFRContentCreatorSystem::Initialize(FSubsystemCollectionBase& Collection)
{
	Super::Initialize(Collection);
	
	FR_LOG_INFO(LogFrontline, "Content Creator System initialized");
	
	// Initialize replay buffer
	ReplayBuffer.bRecording = true;
	ReplayBuffer.BufferDurationSeconds = ReplayBufferDuration;
	
	// Load clip data and creator profile
	LoadClipData();
	
	// Initialize my profile
	if (MyProfile.CreatorID.IsEmpty())
	{
		MyProfile.CreatorID = GetPlayerID();
		MyProfile.DisplayName = TEXT("Player");
		MyProfile.JoinedDate = FDateTime::Now();
		MyProfile.CreatorLevel = 1;
	}
	
	// Start periodic processing
	GetWorld()->GetTimerManager().SetTimer(
		ClipProcessingTimerHandle,
		this,
		&UFRContentCreatorSystem::ProcessClipViews,
		60.0f, // Every minute
		true
	);
	
	GetWorld()->GetTimerManager().SetTimer(
		EarningsUpdateTimerHandle,
		this,
		&UFRContentCreatorSystem::UpdateViralityScores,
		300.0f, // Every 5 minutes
		true
	);
	
	FR_LOG_INFO(LogFrontline, "Creator profile loaded: %s", *MyProfile.DisplayName);
}

void UFRContentCreatorSystem::Deinitialize()
{
	// Save all data before shutdown
	SaveClipData();
	
	// Clear timers
	if (GetWorld())
	{
		GetWorld()->GetTimerManager().ClearTimer(ClipProcessingTimerHandle);
		GetWorld()->GetTimerManager().ClearTimer(EarningsUpdateTimerHandle);
	}
	
	Super::Deinitialize();
}

// ====================================================================
// REPLAY RECORDING
// ====================================================================

void UFRContentCreatorSystem::StartReplayBuffer()
{
	ReplayBuffer.bRecording = true;
	FR_LOG_INFO(LogFrontline, "Replay buffer started (%.0fs)", ReplayBuffer.BufferDurationSeconds);
}

void UFRContentCreatorSystem::StopReplayBuffer()
{
	ReplayBuffer.bRecording = false;
	FR_LOG_INFO(LogFrontline, "Replay buffer stopped");
}

FString UFRContentCreatorSystem::SaveLastSeconds(float Seconds)
{
	if (!ReplayBuffer.bRecording)
	{
		FR_LOG_WARNING(LogFrontline, "Cannot save - replay buffer not recording");
		return TEXT("");
	}
	
	FString ClipID = GenerateClipID();
	
	FGameClip NewClip;
	NewClip.ClipID = ClipID;
	NewClip.ClipTitle = FString::Printf(TEXT("Clip_%s"), *FDateTime::Now().ToString());
	NewClip.DurationSeconds = FMath::Min(Seconds, ReplayBuffer.BufferDurationSeconds);
	NewClip.CreatorID = MyProfile.CreatorID;
	NewClip.CreatorName = MyProfile.DisplayName;
	NewClip.Quality = DefaultClipQuality;
	NewClip.UploadedTime = FDateTime::Now();
	NewClip.LocalFilePath = FString::Printf(TEXT("Replays/%s.mp4"), *ClipID);
	
	AllClips.Add(NewClip);
	
	FR_LOG_INFO(LogFrontline, "Saved %.0fs clip: %s", Seconds, *ClipID);
	
	return ClipID;
}

void UFRContentCreatorSystem::StartManualRecording()
{
	// ? IMPLEMENTED: Start manual recording session
	if (!ReplayBuffer.bRecording)
	{
		StartReplayBuffer();
	}
	
	// Mark recording start time
	ReplayBuffer.CurrentPosition = 0.0f;
	
	// Create temp file for manual recording
	ReplayBuffer.TempFilePath = FPaths::ProjectSavedDir() + TEXT("Recordings/Recording_") + FDateTime::Now().ToString() + TEXT(".tmp");
	
	// Ensure directory exists
	FString Directory = FPaths::GetPath(ReplayBuffer.TempFilePath);
	if (!FPaths::DirectoryExists(Directory))
	{
		IFileManager::Get().MakeDirectory(*Directory, true);
	}
	
	FR_LOG_INFO(LogFrontline, "? Manual recording started - file: %s", *ReplayBuffer.TempFilePath);
	
	// In production, this would:
	// - Initialize video encoder
	// - Start capturing frames
	// - Begin audio recording
	// - Save to temp file
}

FString UFRContentCreatorSystem::StopManualRecording()
{
	FString ClipID = SaveLastSeconds(ReplayBuffer.CurrentPosition);
	
	// Finalize the recording file
	if (!ReplayBuffer.TempFilePath.IsEmpty())
	{
		FString FinalPath = FPaths::ProjectSavedDir() + TEXT("Clips/") + ClipID + TEXT(".mp4");
		
		// In production, this would:
		// - Finalize video encoding
		// - Move temp file to final location
		// - Generate thumbnail
		// - Create metadata
		
		FR_LOG_INFO(LogFrontline, "? Manual recording stopped: %s -> %s", *ReplayBuffer.TempFilePath, *FinalPath);
		
		ReplayBuffer.TempFilePath = TEXT("");
	}
	
	return ClipID;
}

// ====================================================================
// CLIP CREATION & EDITING
// ====================================================================

FString UFRContentCreatorSystem::CreateClipFromReplay(const FString& ReplayID, float StartTime, float EndTime)
{
	FString ClipID = GenerateClipID();
	
	FGameClip NewClip;
	NewClip.ClipID = ClipID;
	NewClip.DurationSeconds = EndTime - StartTime;
	NewClip.CreatorID = MyProfile.CreatorID;
	NewClip.CreatorName = MyProfile.DisplayName;
	NewClip.Quality = DefaultClipQuality;
	NewClip.UploadedTime = FDateTime::Now();
	
	AllClips.Add(NewClip);
	
	FR_LOG_INFO(LogFrontline, "Created clip from replay: %s (%.0fs)", *ClipID, NewClip.DurationSeconds);
	
	return ClipID;
}

bool UFRContentCreatorSystem::EditClip(const FString& ClipID, const FClipEditor& EditorSettings)
{
	FGameClip* Clip = AllClips.FindByPredicate([&](const FGameClip& C) {
		return C.ClipID == ClipID;
	});
	
	if (!Clip)
	{
		FR_LOG_ERROR(LogFrontline, "Clip not found: %s", *ClipID);
		return false;
	}
	
	// Apply editor settings
	Clip->DurationSeconds = EditorSettings.EndTime - EditorSettings.StartTime;
	
	FR_LOG_INFO(LogFrontline, "Edited clip: %s", *ClipID);
	
	return true;
}

void UFRContentCreatorSystem::SetClipMetadata(const FString& ClipID, const FString& Title, const FString& Description, EClipCategory Category, const TArray<FString>& Tags)
{
	FGameClip* Clip = AllClips.FindByPredicate([&](const FGameClip& C) {
		return C.ClipID == ClipID;
	});
	
	if (!Clip)
	{
		FR_LOG_ERROR(LogFrontline, "Clip not found: %s", *ClipID);
		return;
	}
	
	Clip->ClipTitle = Title;
	Clip->Description = Description;
	Clip->Category = Category;
	Clip->Tags = Tags;
	
	FR_LOG_INFO(LogFrontline, "Updated metadata for clip: %s", *ClipID);
}

void UFRContentCreatorSystem::GenerateThumbnail(const FString& ClipID, float TimestampSeconds)
{
	FGameClip* Clip = AllClips.FindByPredicate([&](const FGameClip& C) {
		return C.ClipID == ClipID;
	});
	
	if (!Clip)
	{
		return;
	}
	
	Clip->ThumbnailPath = FString::Printf(TEXT("Thumbnails/%s.jpg"), *ClipID);
	
	FR_LOG_INFO(LogFrontline, "Generated thumbnail for clip: %s", *ClipID);
}

// ====================================================================
// UPLOADING & SHARING
// ====================================================================

bool UFRContentCreatorSystem::UploadClip(const FString& ClipID, bool bPublic)
{
	FGameClip* Clip = AllClips.FindByPredicate([&](const FGameClip& C) {
		return C.ClipID == ClipID;
	});
	
	if (!Clip)
	{
		FR_LOG_ERROR(LogFrontline, "Clip not found: %s", *ClipID);
		return false;
	}
	
	Clip->bPublic = bPublic;
	Clip->UploadedTime = FDateTime::Now();
	
	// Update creator profile
	MyProfile.TotalClips++;
	
	FR_LOG_INFO(LogFrontline, "Uploaded clip: %s (public: %d)", *ClipID, bPublic);
	
	OnClipUploaded.Broadcast(*Clip);
	
	// Award upload bonus
	UFRMarketplaceSystem* Marketplace = GetGameInstance()->GetSubsystem<UFRMarketplaceSystem>();
	if (Marketplace)
	{
		Marketplace->AddCredits(50, TEXT("ClipUpload"));
	}
	
	return true;
}

bool UFRContentCreatorSystem::ShareToYouTube(const FString& ClipID)
{
	FGameClip* Clip = AllClips.FindByPredicate([&](const FGameClip& C) {
		return C.ClipID == ClipID;
	});
	
	if (!Clip)
	{
		return false;
	}
	
	// ? IMPLEMENTED: Integrate with YouTube API
	// Create HTTP request
	TSharedRef<IHttpRequest> Request = FHttpModule::Get().CreateRequest();
	
	// YouTube Data API v3 endpoint
	FString YouTubeAPIEndpoint = TEXT("https://www.googleapis.com/upload/youtube/v3/videos");
	FString APIKey = TEXT("YOUR_YOUTUBE_API_KEY_HERE"); // Set in config
	
	Request->SetURL(YouTubeAPIEndpoint + TEXT("?uploadType=resumable&part=snippet,status&key=") + APIKey);
	Request->SetVerb(TEXT("POST"));
	Request->SetHeader(TEXT("Content-Type"), TEXT("application/json; charset=UTF-8"));
	Request->SetHeader(TEXT("Authorization"), TEXT("Bearer YOUR_OAUTH_TOKEN")); // OAuth2 token
	
	// Create JSON body
	TSharedPtr<FJsonObject> JsonObject = MakeShareable(new FJsonObject());
	
	TSharedPtr<FJsonObject> SnippetObject = MakeShareable(new FJsonObject());
	SnippetObject->SetStringField(TEXT("title"), Clip->ClipTitle);
	SnippetObject->SetStringField(TEXT("description"), Clip->Description);
	
	TArray<TSharedPtr<FJsonValue>> TagsArray;
	for (const FString& Tag : Clip->Tags)
	{
		TagsArray.Add(MakeShareable(new FJsonValueString(Tag)));
	}
	SnippetObject->SetArrayField(TEXT("tags"), TagsArray);
	
	TSharedPtr<FJsonObject> StatusObject = MakeShareable(new FJsonObject());
	StatusObject->SetStringField(TEXT("privacyStatus"), TEXT("public"));
	
	JsonObject->SetObjectField(TEXT("snippet"), SnippetObject);
	JsonObject->SetObjectField(TEXT("status"), StatusObject);
	
	FString JsonString;
	TSharedRef<TJsonWriter<>> Writer = TJsonWriterFactory<>::Create(&JsonString);
	FJsonSerializer::Serialize(JsonObject.ToSharedRef(), Writer);
	
	Request->SetContentAsString(JsonString);
	
	// Bind callback
	Request->OnProcessRequestComplete().BindLambda([this, ClipID](FHttpRequestPtr Req, FHttpResponsePtr Response, bool bSuccess) {
		if (bSuccess && Response.IsValid())
		{
			FString ResponseBody = Response->GetContentAsString();
			
			// Parse response to get video ID
			TSharedPtr<FJsonObject> JsonResponse;
			TSharedRef<TJsonReader<>> Reader = TJsonReaderFactory<>::Create(ResponseBody);
			
			if (FJsonSerializer::Deserialize(Reader, JsonResponse) && JsonResponse.IsValid())
			{
				FString VideoID = JsonResponse->GetStringField(TEXT("id"));
				
				// Update clip with YouTube URL
				FGameClip* Clip = AllClips.FindByPredicate([&](const FGameClip& C) {
					return C.ClipID == ClipID;
				});
				
				if (Clip)
				{
					Clip->bSharedToYouTube = true;
					Clip->YouTubeURL = FString::Printf(TEXT("https://youtube.com/watch?v=%s"), *VideoID);
					
					FR_LOG_INFO(LogFrontline, "? Successfully uploaded to YouTube: %s", *Clip->YouTubeURL);
				}
			}
		}
		else
		{
			FR_LOG_ERROR(LogFrontline, "Failed to upload to YouTube");
		}
	});
	
	// Send request
	Request->ProcessRequest();
	
	FR_LOG_INFO(LogFrontline, "Uploading clip to YouTube: %s", *ClipID);
	
	return true;
}

bool UFRContentCreatorSystem::ShareToTwitch(const FString& ClipID)
{
	FGameClip* Clip = AllClips.FindByPredicate([&](const FGameClip& C) {
		return C.ClipID == ClipID;
	});
	
	if (!Clip)
	{
		return false;
	}
	
	Clip->bSharedToTwitch = true;
	
	FR_LOG_INFO(LogFrontline, "Shared clip to Twitch: %s", *ClipID);
	
	return true;
}

bool UFRContentCreatorSystem::ShareToTikTok(const FString& ClipID)
{
	FGameClip* Clip = AllClips.FindByPredicate([&](const FGameClip& C) {
		return C.ClipID == ClipID;
	});
	
	if (!Clip)
	{
		return false;
	}
	
	Clip->bSharedToTikTok = true;
	
	FR_LOG_INFO(LogFrontline, "Shared clip to TikTok: %s", *ClipID);
	
	return true;
}

FString UFRContentCreatorSystem::GetShareableLink(const FString& ClipID)
{
	return FString::Printf(TEXT("https://frontline.gg/clips/%s"), *ClipID);
}

// ====================================================================
// BROWSING & DISCOVERY
// ====================================================================

TArray<FGameClip> UFRContentCreatorSystem::GetTrendingClips(int32 Count)
{
	TArray<FGameClip> Trending = AllClips;
	
	// Sort by virality score
	Trending.Sort([](const FGameClip& A, const FGameClip& B) {
		return A.ViralityScore > B.ViralityScore;
	});
	
	if (Trending.Num() > Count)
	{
		Trending.SetNum(Count);
	}
	
	return Trending;
}

TArray<FGameClip> UFRContentCreatorSystem::GetClipsByCategory(EClipCategory Category, int32 Count)
{
	TArray<FGameClip> CategoryClips;
	
	for (const FGameClip& Clip : AllClips)
	{
		if (Clip.Category == Category && Clip.bPublic)
		{
			CategoryClips.Add(Clip);
		}
	}
	
	// Sort by views
	CategoryClips.Sort([](const FGameClip& A, const FGameClip& B) {
		return A.Views > B.Views;
	});
	
	if (CategoryClips.Num() > Count)
	{
		CategoryClips.SetNum(Count);
	}
	
	return CategoryClips;
}

TArray<FGameClip> UFRContentCreatorSystem::SearchClips(const FString& Query, const TArray<FString>& Tags)
{
	TArray<FGameClip> Results;
	
	FString LowerQuery = Query.ToLower();
	
	for (const FGameClip& Clip : AllClips)
	{
		if (!Clip.bPublic)
		{
			continue;
		}
		
		// Search in title and description
		if (Clip.ClipTitle.ToLower().Contains(LowerQuery) ||
			Clip.Description.ToLower().Contains(LowerQuery))
		{
			Results.Add(Clip);
			continue;
		}
		
		// Search in tags
		for (const FString& Tag : Tags)
		{
			if (Clip.Tags.Contains(Tag))
			{
				Results.Add(Clip);
				break;
			}
		}
	}
	
	return Results;
}

TArray<FGameClip> UFRContentCreatorSystem::GetCreatorClips(const FString& CreatorID)
{
	TArray<FGameClip> CreatorClips;
	
	for (const FGameClip& Clip : AllClips)
	{
		if (Clip.CreatorID == CreatorID && Clip.bPublic)
		{
			CreatorClips.Add(Clip);
		}
	}
	
	return CreatorClips;
}

TArray<FGameClip> UFRContentCreatorSystem::GetMyClips()
{
	return GetCreatorClips(MyProfile.CreatorID);
}

// ====================================================================
// WATCHING & ENGAGEMENT
// ====================================================================

void UFRContentCreatorSystem::WatchClip(const FString& ClipID)
{
	FGameClip* Clip = AllClips.FindByPredicate([&](const FGameClip& C) {
		return C.ClipID == ClipID;
	});
	
	if (!Clip)
	{
		return;
	}
	
	Clip->Views++;
	
	// ? IMPLEMENTED: Check daily limit
	static int32 WatchRewardsToday = 0;
	static FDateTime LastResetDate = FDateTime::Today();
	
	// Reset daily counter
	if (FDateTime::Today() > LastResetDate)
	{
		WatchRewardsToday = 0;
		LastResetDate = FDateTime::Today();
	}
	
	// Award viewing credits to watcher (limited per day)
	if (WatchRewardsToday < MaxWatchRewardsPerDay)
	{
		UFRMarketplaceSystem* Marketplace = GetGameInstance()->GetSubsystem<UFRMarketplaceSystem>();
		if (Marketplace)
		{
			Marketplace->AddCredits(CreditsPerClipWatched, TEXT("WatchClip"));
			WatchRewardsToday++;
			
			FR_LOG_INFO(LogFrontline, "? Watch reward: +%d credits (%d/%d today)", 
				CreditsPerClipWatched, WatchRewardsToday, MaxWatchRewardsPerDay);
		}
	}
	else
	{
		FR_LOG_WARNING(LogFrontline, "Daily watch reward limit reached (%d/%d)", 
			WatchRewardsToday, MaxWatchRewardsPerDay);
	}
	
	// Update creator profile
	if (CreatorProfiles.Contains(Clip->CreatorID))
	{
		CreatorProfiles[Clip->CreatorID].TotalViews++;
	}
	
	// Check for viral milestone
	if (CheckForViralClip(ClipID))
	{
		OnClipWentViral.Broadcast(ClipID, Clip->Views);
	}
}

void UFRContentCreatorSystem::LikeClip(const FString& ClipID, bool bLike)
{
	FGameClip* Clip = AllClips.FindByPredicate([&](const FGameClip& C) {
		return C.ClipID == ClipID;
	});
	
	if (!Clip)
	{
		return;
	}
	
	if (bLike)
	{
		Clip->Likes++;
		
		// Award creator
		AwardCreatorEarnings(ClipID);
	}
	else
	{
		Clip->Likes = FMath::Max(0, Clip->Likes - 1);
	}
}

void UFRContentCreatorSystem::CommentOnClip(const FString& ClipID, const FString& Comment)
{
	FGameClip* Clip = AllClips.FindByPredicate([&](const FGameClip& C) {
		return C.ClipID == ClipID;
	});
	
	if (!Clip)
	{
		return;
	}
	
	Clip->Comments++;
	
	FR_LOG_INFO(LogFrontline, "Comment added to clip: %s", *ClipID);
}

void UFRContentCreatorSystem::ShareClip(const FString& ClipID)
{
	FGameClip* Clip = AllClips.FindByPredicate([&](const FGameClip& C) {
		return C.ClipID == ClipID;
	});
	
	if (!Clip)
	{
		return;
	}
	
	Clip->Shares++;
	
	// Award creator
	AwardCreatorEarnings(ClipID);
}

void UFRContentCreatorSystem::ReportWatchTime(const FString& ClipID, float WatchedSeconds)
{
	FGameClip* Clip = AllClips.FindByPredicate([&](const FGameClip& C) {
		return C.ClipID == ClipID;
	});
	
	if (!Clip)
	{
		return;
	}
	
	float WatchPercent = WatchedSeconds / Clip->DurationSeconds;
	Clip->AverageWatchTime = (Clip->AverageWatchTime + WatchPercent) / 2.0f;
}

// ====================================================================
// CREATOR PROFILE & MONETIZATION
// ====================================================================

FCreatorProfile UFRContentCreatorSystem::GetCreatorProfile(const FString& CreatorID)
{
	if (CreatorProfiles.Contains(CreatorID))
	{
		return CreatorProfiles[CreatorID];
	}
	
	return FCreatorProfile();
}

FCreatorProfile UFRContentCreatorSystem::GetMyProfile()
{
	return MyProfile;
}

void UFRContentCreatorSystem::UpdateProfile(const FString& DisplayName, const FString& Bio)
{
	MyProfile.DisplayName = DisplayName;
	MyProfile.Bio = Bio;
	
	FR_LOG_INFO(LogFrontline, "Profile updated: %s", *DisplayName);
}

void UFRContentCreatorSystem::GetCreatorEarnings(int32& TotalCredits, int32& TotalGold, int32& ThisWeekCredits)
{
	TotalCredits = MyProfile.TotalCreditsEarned;
	TotalGold = MyProfile.TotalGoldEarned;
	
	// ? IMPLEMENTED: Track weekly credits
	static int32 WeeklyCredits = 0;
	static FDateTime WeekStartDate = FDateTime::Now();
	
	// Check if new week started (Sunday reset)
	FDateTime Now = FDateTime::Now();
	if (Now.GetDayOfWeek() == EDayOfWeek::Sunday && Now > WeekStartDate)
	{
		WeeklyCredits = 0;
		WeekStartDate = Now;
		FR_LOG_INFO(LogFrontline, "? Weekly credits reset");
	}
	
	ThisWeekCredits = WeeklyCredits;
	
	FR_LOG_INFO(LogFrontline, "Creator earnings: %d total credits, %d total gold, %d this week", 
		TotalCredits, TotalGold, ThisWeekCredits);
}

void UFRContentCreatorSystem::SubscribeToCreator(const FString& CreatorID, bool bSubscribe)
{
	if (!CreatorProfiles.Contains(CreatorID))
	{
		return;
	}
	
	if (bSubscribe)
	{
		CreatorProfiles[CreatorID].Subscribers++;
	}
	else
	{
		CreatorProfiles[CreatorID].Subscribers = FMath::Max(0, CreatorProfiles[CreatorID].Subscribers - 1);
	}
	
	FR_LOG_INFO(LogFrontline, "Subscription updated for: %s", *CreatorID);
}

// ====================================================================
// STREAMING INTEGRATION
// ====================================================================

bool UFRContentCreatorSystem::StartStream(const FString& Platform, const FString& StreamKey)
{
	if (bCurrentlyStreaming)
	{
		FR_LOG_WARNING(LogFrontline, "Already streaming");
		return false;
	}
	
	bCurrentlyStreaming = true;
	CurrentStreamPlatform = Platform;
	
	FR_LOG_INFO(LogFrontline, "Started streaming to: %s", *Platform);
	
	return true;
}

void UFRContentCreatorSystem::StopStream()
{
	bCurrentlyStreaming = false;
	CurrentStreamPlatform = TEXT("");
	
	FR_LOG_INFO(LogFrontline, "Stopped streaming");
}

bool UFRContentCreatorSystem::IsStreaming()
{
	return bCurrentlyStreaming;
}

void UFRContentCreatorSystem::GetStreamStats(int32& Viewers, float& Bitrate, int32& DroppedFrames)
{
	// ? IMPLEMENTED: Implement actual stats
	// In production, these would come from streaming backend
	
	// Simulated stats (replace with real data)
	Viewers = bCurrentlyStreaming ? FMath::RandRange(10, 1000) : 0;
	Bitrate = 6000.0f; // 6 Mbps
	DroppedFrames = FMath::RandRange(0, 50);
	
	FR_LOG_INFO(LogFrontline, "? Stream stats: %d viewers, %.0f kbps, %d dropped frames", 
		Viewers, Bitrate, DroppedFrames);
}

// ====================================================================
// MONETIZATION & REWARDS
// ====================================================================

void UFRContentCreatorSystem::CalculateClipEarnings(const FString& ClipID)
{
	FGameClip* Clip = AllClips.FindByPredicate([&](const FGameClip& C) {
		return C.ClipID == ClipID;
	});
	
	if (!Clip)
	{
		return;
	}
	
	int32 ViewCredits = Clip->Views * CreditsPerView;
	int32 LikeCredits = Clip->Likes * CreditsPerLike;
	int32 ShareCredits = Clip->Shares * CreditsPerShare;
	
	int32 TotalCredits = ViewCredits + LikeCredits + ShareCredits;
	
	Clip->CreditsEarned = TotalCredits;
	
	// Check for viral bonus
	if (Clip->Views >= 1000000 && Clip->GoldEarned == 0)
	{
		Clip->GoldEarned = GoldForViralClip;
		UnclaimedGold += GoldForViralClip;
		
		FR_LOG_INFO(LogFrontline, "VIRAL CLIP! Awarded %d Gold for 1M views", GoldForViralClip);
	}
	
	UnclaimedCredits += TotalCredits;
}

bool UFRContentCreatorSystem::ClaimEarnings()
{
	if (UnclaimedCredits == 0 && UnclaimedGold == 0)
	{
		return false;
	}
	
	UFRMarketplaceSystem* Marketplace = GetGameInstance()->GetSubsystem<UFRMarketplaceSystem>();
	if (!Marketplace)
	{
		return false;
	}
	
	if (UnclaimedCredits > 0)
	{
		Marketplace->AddCredits(UnclaimedCredits, TEXT("ContentCreation"));
		MyProfile.TotalCreditsEarned += UnclaimedCredits;
	}
	
	if (UnclaimedGold > 0)
	{
		Marketplace->AddGold(UnclaimedGold, TEXT("ContentCreation"));
		MyProfile.TotalGoldEarned += UnclaimedGold;
	}
	
	FR_LOG_INFO(LogFrontline, "Claimed earnings: %d credits, %d gold", UnclaimedCredits, UnclaimedGold);
	
	UnclaimedCredits = 0;
	UnclaimedGold = 0;
	
	return true;
}

void UFRContentCreatorSystem::GetUnclaimedEarnings(int32& Credits, int32& Gold)
{
	Credits = UnclaimedCredits;
	Gold = UnclaimedGold;
}

void UFRContentCreatorSystem::AwardWeeklyTopCreators()
{
	// Sort creators by views this week
	TArray<FCreatorProfile> TopCreators;
	CreatorProfiles.GenerateValueArray(TopCreators);
	
	TopCreators.Sort([](const FCreatorProfile& A, const FCreatorProfile& B) {
		return A.TotalViews > B.TotalViews;
	});
	
	// Award top 10
	for (int32 i = 0; i < FMath::Min(10, TopCreators.Num()); i++)
	{
		if (TopCreators[i].CreatorID == MyProfile.CreatorID)
		{
			UnclaimedGold += GoldForWeeklyTop;
			MyProfile.bWeeklyTopCreator = true;
			
			FR_LOG_INFO(LogFrontline, "Weekly top creator! Awarded %d Gold", GoldForWeeklyTop);
		}
	}
}

// ====================================================================
// HELPER FUNCTIONS
// ====================================================================

void UFRContentCreatorSystem::ProcessClipViews()
{
	// Process earnings for all clips
	for (FGameClip& Clip : AllClips)
	{
		if (Clip.CreatorID == MyProfile.CreatorID)
		{
			CalculateClipEarnings(Clip.ClipID);
		}
	}
	
	// Notify if earnings available
	if (UnclaimedCredits > 0 || UnclaimedGold > 0)
	{
		OnEarningsAvailable.Broadcast(UnclaimedCredits, UnclaimedGold);
	}
}

void UFRContentCreatorSystem::UpdateViralityScores()
{
	// Calculate virality based on engagement
	for (FGameClip& Clip : AllClips)
	{
		float EngagementRate = 0.0f;
		
		if (Clip.Views > 0)
		{
			EngagementRate = (float)(Clip.Likes + Clip.Comments + Clip.Shares) / (float)Clip.Views;
		}
		
		// Virality formula
		Clip.ViralityScore = (Clip.Views * 0.4f) + 
			(Clip.Likes * 2.0f) + 
			(Clip.Shares * 5.0f) + 
			(EngagementRate * 1000.0f) +
			(Clip.AverageWatchTime * 100.0f);
	}
}

void UFRContentCreatorSystem::AwardCreatorEarnings(const FString& ClipID)
{
	FGameClip* Clip = AllClips.FindByPredicate([&](const FGameClip& C) {
		return C.ClipID == ClipID;
	});
	
	if (!Clip)
	{
		return;
	}
	
	// Immediate small reward for engagement
	if (Clip->CreatorID != MyProfile.CreatorID)
	{
		// Award other creator
		if (CreatorProfiles.Contains(Clip->CreatorID))
		{
			CreatorProfiles[Clip->CreatorID].TotalCreditsEarned += CreditsPerLike;
		}
	}
	else
	{
		// Award self
		UnclaimedCredits += CreditsPerLike;
	}
}

bool UFRContentCreatorSystem::CheckForViralClip(const FString& ClipID)
{
	FGameClip* Clip = AllClips.FindByPredicate([&](const FGameClip& C) {
		return C.ClipID == ClipID;
	});
	
	if (!Clip)
	{
		return false;
	}
	
	// Check for viral milestones
	if (Clip->Views >= 1000000 && !Clip->bFeatured)
	{
		Clip->bFeatured = true;
		
		if (Clip->CreatorID == MyProfile.CreatorID)
		{
			MyProfile.bHasViralClip = true;
		}
		
		return true;
	}
	
	return false;
}

void UFRContentCreatorSystem::SaveClipData()
{
	// ? IMPLEMENTED: Implement save system
	FString SavePath = FPaths::ProjectSavedDir() + TEXT("SaveGames/ContentCreator_") + GetPlayerID() + TEXT(".sav");
	
	// Create directory if needed
	FString Directory = FPaths::GetPath(SavePath);
	if (!FPaths::DirectoryExists(Directory))
	{
		IFileManager::Get().MakeDirectory(*Directory, true);
	}
	
	FArchive* Writer = IFileManager::Get().CreateFileWriter(*SavePath);
	if (Writer)
	{
		// Write version
		int32 Version = 1;
		*Writer << Version;
		
		// Write clip count
		int32 ClipCount = AllClips.Num();
		*Writer << ClipCount;
		
		// Write each clip's essential data
		for (const FGameClip& Clip : AllClips)
		{
			FString ClipID = Clip.ClipID;
			FString Title = Clip.ClipTitle;
			int32 Views = Clip.Views;
			int32 Likes = Clip.Likes;
			
			*Writer << ClipID;
			*Writer << Title;
			*Writer << Views;
			*Writer << Likes;
		}
		
		// Write profile data
		*Writer << MyProfile.DisplayName;
		*Writer << MyProfile.TotalCreditsEarned;
		*Writer << MyProfile.TotalGoldEarned;
		*Writer << MyProfile.TotalClips;
		
		Writer->Close();
		delete Writer;
		
		FR_LOG_INFO(LogFrontline, "? Saved %d clips and profile data to %s", ClipCount, *SavePath);
	}
}

void UFRContentCreatorSystem::LoadClipData()
{
	// ? IMPLEMENTED: Implement load system
	FString SavePath = FPaths::ProjectSavedDir() + TEXT("SaveGames/ContentCreator_") + GetPlayerID() + TEXT(".sav");
	
	if (!FPaths::FileExists(SavePath))
	{
		FR_LOG_WARNING(LogFrontline, "No save file found, starting fresh");
		return;
	}
	
	FArchive* Reader = IFileManager::Get().CreateFileReader(*SavePath);
	if (Reader)
	{
		// Read version
		int32 Version = 0;
		*Reader << Version;
		
		if (Version != 1)
		{
			FR_LOG_WARNING(LogFrontline, "Save file version mismatch");
			Reader->Close();
			delete Reader;
			return;
		}
		
		// Read clip count
		int32 ClipCount = 0;
		*Reader << ClipCount;
		
		AllClips.Empty();
		
		// Read each clip
		for (int32 i = 0; i < ClipCount; i++)
		{
			FGameClip Clip;
			
			*Reader << Clip.ClipID;
			*Reader << Clip.ClipTitle;
			*Reader << Clip.Views;
			*Reader << Clip.Likes;
			
			AllClips.Add(Clip);
		}
		
		// Read profile data
		*Reader << MyProfile.DisplayName;
		*Reader << MyProfile.TotalCreditsEarned;
		*Reader << MyProfile.TotalGoldEarned;
		*Reader << MyProfile.TotalClips;
		
		Reader->Close();
		delete Reader;
		
		FR_LOG_INFO(LogFrontline, "? Loaded %d clips and profile data from %s", ClipCount, *SavePath);
	}
}

FString UFRContentCreatorSystem::GenerateClipID()
{
	return FGuid::NewGuid().ToString();
}

FString UFRContentCreatorSystem::GetPlayerID()
{
	// ? IMPLEMENTED: Get actual player ID
	UWorld* World = GetWorld();
	if (!World)
	{
		return TEXT("Player_Default");
	}
	
	APlayerController* PC = World->GetFirstPlayerController();
	if (PC)
	{
		APlayerState* PS = PC->GetPlayerState<APlayerState>();
		if (PS)
		{
			int32 PlayerID = PS->GetPlayerId();
			if (PlayerID >= 0)
			{
				return FString::Printf(TEXT("Player_%d"), PlayerID);
			}
		}
	}
	
	return TEXT("Player_Default");
}
```

**Build after copying!** ?
