import { Page, PageSection } from "@/components/page";
import { EyecatchCard } from "@/components/introduction/card/eyecatch-card";
import { FeatureCardList } from "@/components/introduction/card/feature-card-list";

export default function Home() {
	return (
		<Page>
			<PageSection id={"eyecatch"}>
				<EyecatchCard />
			</PageSection>
			<PageSection id={"feature"}>
				<FeatureCardList />
			</PageSection>
		</Page>
	);
}
